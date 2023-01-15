#!/bin/zsh

function usage() {
  echo "Usage: ./commands.zsh [keyword]" 1>&2
  exit 1
}

#osascript -e 'display dialog "Hello from osxdaily.com" with title
osascript -e 'tell application id "com.runningwithcrayons.Alfred" to run trigger "update" in workflow "com.vegardlandsverk.bluetoothcontroller"'

case "$1" in
  set_favorite)       ./scripts/set_favorite.zsh ;;
  remove_favorite)    ./scripts/remove_favorite.zsh ;;
  connect_favorite)   ./scripts/connect_favorite.py ;;
  unpair)             ./scripts/unpair.py ;;
  connect)            ./scripts/connect.py ;;
  pair)               ./scripts/pair.py ;;
  off)                ./scripts/toggle.zsh -p 0 ;;
  on)                 ./scripts/toggle.zsh -p 1 ;;
  toggle)             ./scripts/toggle.zsh -t ;;
  reset)              ./scripts/toggle.zsh -r ;;
  large_type)         ./scripts/large_type.zsh ;;
  *)                   usage ;;
esac

if [ -z "$1" ]; then
  usage
fi
