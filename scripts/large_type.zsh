t a#!/bin/zsh

echo "POWER"
echo | ./blueutil --power
echo ""
echo "DISCOVERABLE"
echo | ./blueutil --discoverable
echo ""
echo "CONNECTED"
echo | ./blueutil --connected | cut -d '"' -f 2
echo ""
echo "PAIRED"
echo | ./blueutil --paired | grep -v '"-"' | cut -d '"' -f 2