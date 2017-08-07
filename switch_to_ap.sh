#!/bin/bash

sudo cp ./interfaces.ap /etc/network/interfaces
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo reboot
