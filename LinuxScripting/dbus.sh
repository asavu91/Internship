#!/bin/bash


status=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep -E "state" | awk '{print $2}')

if [ "$status" == "charging" ] || [ "$status" == "fully-charged" ]; then
    echo "Status: $status"
elif [[ "$status" == "discharging" ]]; then
    echo "The machine is currently using the battery"
else
    echo "Battery not found"
fi

