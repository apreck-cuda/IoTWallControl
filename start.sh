#!/bin/bash

LOG=/var/log/start_$(date +%y_%m_%d_%H_%M).log

echo $(date) "Initializing GPIOs" >> $LOG

echo 106 > /sys/class/gpio/export
echo 107 > /sys/class/gpio/export
echo 108 > /sys/class/gpio/export
echo 109 > /sys/class/gpio/export
echo 110 > /sys/class/gpio/export
echo 111 > /sys/class/gpio/export
echo 112 > /sys/class/gpio/export
echo 113 > /sys/class/gpio/export

echo "in" > /sys/class/gpio/gpio106/direction
echo "in" > /sys/class/gpio/gpio107/direction
echo "in" > /sys/class/gpio/gpio108/direction
echo "in" > /sys/class/gpio/gpio109/direction
echo "out" > /sys/class/gpio/gpio110/direction
echo "out" > /sys/class/gpio/gpio111/direction
echo "out" > /sys/class/gpio/gpio112/direction
echo "out" > /sys/class/gpio/gpio113/direction

echo $(date) "Initialization completed sending verification  sequence" >> $LOG

echo 1 > /sys/class/gpio/gpio110/value
sleep 1
echo 0 > /sys/class/gpio/gpio110/value
sleep 1
echo 1 > /sys/class/gpio/gpio111/value
sleep 1
echo 0 > /sys/class/gpio/gpio111/value
sleep 1
echo 1 > /sys/class/gpio/gpio112/value
sleep 1
echo 0 > /sys/class/gpio/gpio112/value
sleep 1
echo 1 > /sys/class/gpio/gpio113/value
sleep 1
echo 0 > /sys/class/gpio/gpio113/value

echo $(date) "Starting python application" >> $LOG

screen -dmS apipy python3 /opt/iotcontrol/apiworker.py >> $LOG

if [ "$?" -eq "0" ]
then
        echo $(date) "API worker is running check screen apipy for logs " >> $LOG
else
        echo $(date) "Failed to run API worker" >> $LOG
fi

#GPIO in order to control need to add this to /opt/phion/config/template.conf
#lxc.mount.entry=/sys/class/gpio     sys/class/gpio  none    rw,bind     0   0
#lxc.mount.entry=/sys/devices        sys/devices     none    rw,bind     0   0