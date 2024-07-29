#!/bin/zsh

power="POWER\n"$(blueutil --power)
disc="DISCOVERABLE\n"$(blueutil --discoverable)
conn="CONNECTED\n"$(blueutil --connected | cut -d '"' -f 2)
paired="PAIRED\n"$(blueutil --paired | grep -v '"-"' | cut -d '"' -f 2)

bt_status=$power'\n\n'$disc'\n\n'$conn'\n\n'$paired
osascript -e 'tell application id "com.runningwithcrayons.Alfred" to run trigger "large_type" in workflow "com.vegardlandsverk.bluetoothcontroller" with argument "'"$bt_status"'"'
