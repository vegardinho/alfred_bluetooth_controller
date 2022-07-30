#!/usr/bin/python3
# encoding: utf-8

import os
from subprocess import run, PIPE
from script_output import script_output

UID = os.environ['uid']
DEV_NAME = os.environ['device_name']


def main():
    notify_connecting()
    ret_val = get_status()
    store_variables(ret_val)


#	Return	0	Successfully connected	
# 			1	Successfully disconnected
# 			2	Error
def get_status():
    # Turn on bluetooth if turned off
    if run('./blueutil --power'.split(), stdout=PIPE).returncode == 0:
        run('./blueutil --power 1; sleep 1'.split())

    # Disconnect if connected
    if run(f'./blueutil --is-connected {UID}'.split(), stdout=PIPE).returncode == 1:
        # Report error if not successfull disconnect
        if run(f'./blueutil --disconnect {UID} --info {UID}'.split(), stdout=PIPE).returncode != 0:
            return 2
        return 1

    # Try to connect
    if run(f'./blueutil --connect {UID}'.split(), stdout=PIPE).returncode == 1:
        return 2

    return 0


def store_variables(text_ind):
    title_vars = [
        ['Successfully connected to bluetooth device', f'Connected to \'{DEV_NAME}\''],
        ['Bluetooth device successfully disconnected', f'Disconnected from \'{DEV_NAME}\''],
        [f'Failed to toggle connection with \'{DEV_NAME}\'',
         'Make sure the device is turned on and within range, and try again']
    ]

    store_vars = {'not_title': title_vars[text_ind][0], 'not_subtitle': title_vars[text_ind][1]}

    script_output(**store_vars)


if __name__ == '__main__':
    main()
