# Copyright 2018 Bowen Zhang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import smbus
import time

from ctypes import c_short


def _convertToString(data):
  # Simple function to convert binary data into
  # a string
  return str((data[1] + (256 * data[0])) / 1.2)


def _getShort(data, index):
  # return two bytes from data as a signed 16-bit value
  return c_short((data[index] << 8) + data[index + 1]).value


def _getUshort(data, index):
  # return two bytes from data as an unsigned 16-bit value
  return (data[index] << 8) + data[index + 1]


class BarometricSensor(object):

  _DEVICE = 0x77  # Default device I2C address
  _CHIP_ID_REG_ID = 0xD0
  # Register Addresses
  _REG_CALIB = 0xAA
  _REG_MEAS = 0xF4
  _REG_MSB = 0xF6
  _REG_LSB = 0xF7
  # Control Register Address
  _CRV_TEMP = 0x2E
  _CRV_PRES = 0x34
  # Oversample setting
  _OVERSAMPLE = 3  # 0 - 3

  def __init__(self):
    self._bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
    self._id, self._version = self._bus.read_i2c_block_data(
        self._DEVICE, self._CHIP_ID_REG_ID, 2)
    self._temperature = None
    self._pressure = None

  @property
  def chip_id(self):
    return self._id

  @property
  def chip_version(self):
    return self._version

  @property
  def temperature(self):
    """Gets temperature in Celsius."""
    return self._temperature

  @property
  def pressure(self):
    """Gets pressure in Pa."""
    return self._pressure

  def read(self):
    # Read calibration data from EEPROM
    cal = self._bus.read_i2c_block_data(self._DEVICE, self._REG_CALIB, 22)

    # Convert byte data to word values
    AC1 = _getShort(cal, 0)
    AC2 = _getShort(cal, 2)
    AC3 = _getShort(cal, 4)
    AC4 = _getUshort(cal, 6)
    AC5 = _getUshort(cal, 8)
    AC6 = _getUshort(cal, 10)
    B1 = _getShort(cal, 12)
    B2 = _getShort(cal, 14)
    MB = _getShort(cal, 16)
    MC = _getShort(cal, 18)
    MD = _getShort(cal, 20)

    # Read temperature
    self._bus.write_byte_data(self._DEVICE, self._REG_MEAS, self._CRV_TEMP)
    time.sleep(0.005)
    (msb, lsb) = self._bus.read_i2c_block_data(self._DEVICE, self._REG_MSB, 2)
    UT = (msb << 8) + lsb

    # Read pressure
    self._bus.write_byte_data(self._DEVICE, self._REG_MEAS,
                              self._CRV_PRES + (self._OVERSAMPLE << 6))
    time.sleep(0.04)
    (msb, lsb, xsb) = self._bus.read_i2c_block_data(self._DEVICE,
                                                    self._REG_MSB, 3)
    UP = ((msb << 16) + (lsb << 8) + xsb) >> (8 - self._OVERSAMPLE)

    # Refine temperature
    X1 = ((UT - AC6) * AC5) >> 15
    X2 = (MC << 11) / (X1 + MD)
    B5 = X1 + X2
    self._temperature = ((int(B5 + 8) >> 4) / 10.0 * 9 / 5) + 32

    # Refine pressure
    B6 = B5 - 4000
    B62 = int(B6 * B6) >> 12
    X1 = (B2 * B62) >> 11
    X2 = int(AC2 * B6) >> 11
    X3 = X1 + X2
    B3 = (((AC1 * 4 + X3) << self._OVERSAMPLE) + 2) >> 2

    X1 = int(AC3 * B6) >> 13
    X2 = (B1 * B62) >> 16
    X3 = ((X1 + X2) + 2) >> 2
    B4 = (AC4 * (X3 + 32768)) >> 15
    B7 = (UP - B3) * (50000 >> self._OVERSAMPLE)

    P = (B7 * 2) / B4

    X1 = (int(P) >> 8) * (int(P) >> 8)
    X1 = (X1 * 3038) >> 16
    X2 = int(-7357 * P) >> 16
    self._pressure = int(P + ((X1 + X2 + 3791) >> 4))
