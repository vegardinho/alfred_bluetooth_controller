#!/usr/bin/python3
# encoding: utf-8

import os
from subprocess import run, check_output, CalledProcessError
from notify import notify


def connect(uid, dev_name):
    notify_connecting(dev_name)
    try:
        ret_val = get_status(uid)
    except CalledProcessError:
        ret_val = 2
    notify_finished(ret_val, dev_name)


#	Return	0	Successfully connected	
# 			1	Successfully disconnected
# 			2	Error
def get_status(uid):
    # Turn on bluetooth if turned off
    if check_output('./blueutil --power'.split(), text=True).strip() == '0':
        run('./blueutil --power 1'.split())
        run('sleep 1'.split())

    # Disconnect if connected
    if check_output(f'./blueutil --is-connected {uid}'.split(), text=True).strip() == '1':
        # Report error if not successfull disconnect
        # print((f'./blueutil --disconnect {uid}'.split()).returncode)
        if run(f'./blueutil --disconnect {uid} --wait-disconnect {uid}'.split()).returncode != 0:
            return 2
        return 1

    # Try to connect
    if check_output(f'./blueutil --connect {uid}'.split(), text=True).strip() == '1':
        return 2

    return 0


def notify_connecting(dev_name):
    title = f'Toggling connection with {dev_name}'
    message = 'Please wait...'

    notify(title, message)


def notify_finished(text_ind, dev_name):
    out = [
        ['Successfully connected to bluetooth device', f'Connected to {dev_name}'],
        ['Bluetooth device successfully disconnected', f'Disconnected from {dev_name}'],
        [f'Failed to toggle connection with {dev_name}',
         'Make sure the device is turned on and within range, and try again']
    ]

    notify(out[text_ind][0], out[text_ind][1])


# Use environment variable if run as main
if __name__ == '__main__':
    uid = os.environ['uid']
    dev_name = os.environ['device_name']

    connect(uid, dev_name)
