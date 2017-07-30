#!/bin/bash

sudo cp ./interfaces.ap /etc/network/interfaces
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo service hostapd start
sudo service dnsmasq start
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
