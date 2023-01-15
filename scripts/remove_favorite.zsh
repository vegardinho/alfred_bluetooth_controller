#!/bin/zsh

security delete-generic-password -a "alfred-bluetooth-device-id" -s "alfred-bluetooth-device-id"
./notificator --title "Removed favorite device" --message "$device_name removed as favorite" --sound 'Frog'

