#!/bin/zsh


function change_status() {
	./blueutil -p $1

	if [ $1 -eq 0 ]; then
		new_status="OFF"
	else
		new_status="ON"	
	fi

	./notificator --message "Bluetooth $new_status" --sound Frog	
}


function reset() {
	change_status 0
	sleep 3
	change_status 1
}


function toggle() {
	stat=$(./blueutil -p)

	if [ $stat -eq 1 ]; then
		change_status 0
	else
		change_status 1
	fi
}


while getopts tp:r flag
do
    case "${flag}" in
        t) toggle;;
        p) change_status ${OPTARG};;
		r) reset;;
    esac
done
