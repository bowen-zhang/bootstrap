#!/bin/bash

USERDIR=/home/pi
SRCDIR=$USERDIR/src

# Elevate privileges
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

sudo apt-get update
sudo apt-get install python-dev

# Install VIM
sudo apt-get -y install vim

###############################
echo Setting python library path...
if grep -xqe "export PYTHONPATH=.*" $USERDIR/.profile ; then
  sed -i '/^export PYTHONPATH=.*$/d' $USERDIR/.profile
fi
echo "export PYTHONPATH=$SRCDIR" >> $USERDIR/.profile


###############################
echo Optimizing boot performance...
cd $USERDIR
mkdir ./mnt
sudo mount /dev/mmcblk0p1 ./mnt
if [ -e ./mnt/autoboot.txt ]; then
  if grep -xqe "boot_partition=.*" ./mnt/autoboot.txt ; then
    sudo sed -i '/^boot_partition=.*$/d' ./mnt/autoboot.txt
  fi
fi
echo "boot_partition=6" | sudo tee -a ./mnt/autoboot.txt > /dev/null
sudo umount ./mnt
rmdir ./mnt

###########
echo Removing dphys-swapfile
sudo apt-get purge -y dphys-swapfile

###########
echo Disabling unnecessary services
sudo systemctl disable hciuart
sudo systemctl disable dnsmasq
sudo systemctl disable hostapd
sudo systemctl disable triggerhappy
sudo systemctl disable fake-hwclock
sudo systemctl disable plymouth-start
sudo systemctl disable avahi-daemon
sudo systemctl disable kbd

###########
echo Tuning kernel...
sudo cp cmdline.txt /boot/cmdline.txt

echo DONE!

