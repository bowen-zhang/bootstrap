#!/bin/bash

SSID=$1
Password=$2

if [ -z "$SSID" ]; then
  echo 'SSID is not set.'
  exit 1
fi

if [ -z "$Password" ]; then
  echo 'Password is not set.'
  exit 1
fi

#sudo apt-get update
#sudo apt-get -y dist-upgrade
sudo apt-get -y install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd

echo Configuring /etc/dhcpcd.conf...
if ! grep -Fxq "denyinterfaces wlan0" /etc/dhcpcd.conf; then
  echo "denyinterfaces wlan0" | sudo tee -a /etc/dhcpcd.conf > /dev/null
fi

echo Configuring /etc/dnsmasq.conf
sudo cp dnsmasq.conf /etc/dnsmasq.conf

echo Configuring /etc/hostapd.conf...
sudo cp hostapd.conf /etc/hostapd/hostapd.conf
sudo sed -i "s/ssid=.*$/ssid=$SSID/" /etc/hostapd/hostapd.conf
sudo sed -i "s/wpa_passphrase=.*$/wpa_passphrase=$Password/" /etc/hostapd/hostapd.conf
echo Configuring /etc/default/hostapd...
sudo sed -i 's/^#DAEMON_CONF=.*$/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/' /etc/default/hostapd
