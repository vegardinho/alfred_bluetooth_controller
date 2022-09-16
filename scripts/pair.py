#!/usr/bin/python3
# encoding: utf-8

import os
from subprocess import run, PIPE
from notify import notify

UID = os.environ['uid']
DEV_NAME = os.environ['device_name']


#	Return	0	Successfully paired
# 			1	Error
def pair():
    # Turn on bluetooth if turned off
    if run('./blueutil --power'.split(), stdout=PIPE).returncode == 0:
        run('./blueutil --power 1; sleep 1'.split())

    # Disconnect if connected
    if run(f'./blueutil --pair {UID}'.split(), stdout=PIPE).returncode != 0:
        # Report error if not successfull pair
        return 1

    return 0


def main():
    notify_pairing()
    ret_val = pair()
    store_variables(ret_val)


def notify_pairing():
    title = f'Attempting to pair with {DEV_NAME}'
    message = 'Please wait...'

    notify(title, message)


def store_variables(text_ind):
    out = [
        ['Pair successful', f'Successfully paired with {DEV_NAME}'],
        [f'Failed to pair with bluetooth {DEV_NAME}',
         f'Make sure the device is in search mode and within range, and try again'],
    ]

    notify(out[text_ind][0], out[text_ind][1])


if __name__ == '__main__':
    main()