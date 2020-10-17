#!/usr/bin/env bash

echo "Monitoring usb ports"
DISK_MOUNTED=false
POWER_ON=true

echo "Thinkin bout startin neut"
while [ $DISK_MOUNTED = false ]; do
        if [ -d "/media/pi/backup/caperbunny" ]
    then
       echo "Neut has mounted"
       DISK_MOUNTED=true
       eval "python transfer_files.py True"
    fi
done
