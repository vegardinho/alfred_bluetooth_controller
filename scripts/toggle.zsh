#!/bin/zsh

function usage() {
  echo "Usage: ./toggle.zsh [-t] [-p 0|1] [-r]" 1>&2
  exit 1
}

function change_status() {
  blueutil -p "$1"

  if [ $? != 0 ]; then
    new_status="Failed to change bluetooth status. Ensure configuration is correct and blueutil installed."
  elif [ "$1" -eq 0 ]; then
    new_status="Bluetooth OFF"
  else
    new_status="Bluetooth ON"
  fi

  ./notificator --message "$new_status" --sound Frog
}

function reset() {
  change_status 0
  sleep 3
  change_status 1
}

function toggle() {
  stat=$(blueutil -p)

  if [ "$stat" -eq 1 ]; then
    change_status 0
  else
    change_status 1
  fi
}

while getopts tp:r flag; do
  case "${flag}" in
    t) toggle ;;
    p) change_status "${OPTARG}" ;;
    r) reset ;;
    *) usage ;;
  esac
done

if [ -z "${flag}" ]; then
  usage
fi
