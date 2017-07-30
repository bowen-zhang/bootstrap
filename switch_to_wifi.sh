#!/bin/bash

sudo cp ./interfaces.wifi /etc/network/interfaces
sudo cp ./wpa_supplicant.conf.atc /etc/wpa_supplicant/wpa_supplicant.conf

sudo systemctl disable hostapd
sudo systemctl disable dnsmasq
sudo service hostapd stop
sudo service dnsmasq stop
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
