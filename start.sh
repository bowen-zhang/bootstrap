#!/bin/bash

# Elevate privileges
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

# Install VIM
sudo apt-get install vim

# Set python library path
if grep -xqe "PYTHONPATH=.*" $HOME/.profile ; then
  sed -i '/^PYTHONPATH=.*$/d' $HOME/.profile
fi
echo "PYTHONPATH=$HOME/src" >> $HOME/.profile


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