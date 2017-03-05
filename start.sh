#!/bin/bash

# Elevate privileges
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

# Install VIM
sudo apt-get -y install vim

# Set python library path
if grep -xqe "export PYTHONPATH=.*" $HOME/.profile ; then
  sed -i '/^export PYTHONPATH=.*$/d' $HOME/.profile
fi
echo "export PYTHONPATH=$HOME/src" >> $HOME/.profile


# Optimize boot performance
cd $HOME
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

sudo service hciuart stop
sudo service dhcpcd stop
sudo service alsa-restore stop
 
