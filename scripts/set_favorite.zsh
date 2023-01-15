#!/bin/zsh

security add-generic-password -a "alfred-bluetooth-device-id" -s "alfred-bluetooth-device-id" -w "$uid" -C "note" -U
./notificator --title "Favorite device set" --message "$device_name set as favorite device" --sound 'Frog'

