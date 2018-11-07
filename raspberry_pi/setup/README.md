# What

Setting up a Raspberry Pi headless (without monitor and keyboard).

# How

## Before Start

Make sure you have:

* Raspberry Pi (or Raspberry Pi Zero W)
* Micro SD card
* Micro SD card USB reader
* Laptop (Mac, Windows or Linux)
* USB (male to male) cable or [USB to TTL cable](https://www.google.com/search?q=usb+PL2303HX)

## Flash Image

1. Download [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/) image.

1. Unzip the image.

1. Download and install [Etcher](https://www.balena.io/etcher/) app.

1. Flash the image to SD card.

    1. Put micro SD card into USB reader.
    1. Connect USB reader to laptop.
    1. Launch Ether app.
    1. Select the unzipped image file.
    1. Select drive.
    1. Click "Flash".
    1. Once done, disconnect USB reader from laptop.

## Configure Raspbian

1. Put micro SD card into USB reader.

1. Enable SSH

    For Mac:
    ```shell
    touch /Volumes/boot/ssh
    ```

    For Windows:
    ```shell
    cd [SD card drive]:
    type NULL >> ssh
    ```

1. Enable Serial Console

    If you want to use USB to TTL cable to connect to Raspberry Pi, add the
    following to /Volumes/boot/config.txt:
    
    ```
    enable_uart=1
    ```

1. Setup WiFi.

    Create /Volumes/boot/wpa_supplicant.conf with the following content:

    ```
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="NETWORK-NAME"
        psk="NETWORK-PASSWORD"
    }
    ```

    If connecting to a unsure WiFi, add the following in "network":
    ```
    key_mgmt=NONE
    ```

## Boot

1. Put micro SD card into Raspberry Pi.

1. Connect USB to TTL cable

    1. Red wire: DO NOT connect.
    1. Black wire to PIN 6.
    1. White wire to PIN 8.
    1. Green wire to PIN 10.
    1. USB to laptop.

1. Power up by connecting USB to micro USB cable.

## Connect via Serial Console

1. Install driver (for Mac).

    1. Download and install driver from [here](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41).
    1. Reboot.
    1. Open "Security & Privacy", click "Allow".

1. Find USB device.

    ```shell
    ls /dev/cu.*
    ```

    Look for something like "cu.usbserial".

1. Connect to console.

    ```shell
    screen /dev/cu.usbserial 115200
    ```

1. Login

    * username: pi
    * password: raspberry

## Connect via SSH

    Before connecting to a new Raspberry Pi for the first time:
    ```shell
    ssh-keygen -R raspberrypi.local
    ```

    Then, each time:
    ```shell
    ssh pi@raspberrypi.local
    ```

    And use password "raspberry".

## Mount File System

1. (for Mac OS) Install [FUSE and SSHFS for Mac](https://osxfuse.github.io/).

1. Mount remote directory via sshfs

    ```shell
    mkdir ~/[mount point]
    sshfs pi@raspberrypi.local:/home/pi ~/[mount point]
    ```

## Resources

* [Raspberry Pi Pinout](http://www.pighixxx.net/wp-content/uploads/2015/06/raspberry.pdf)