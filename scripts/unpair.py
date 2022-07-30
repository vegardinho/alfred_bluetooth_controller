#!/usr/bin/python3
# encoding: utf-8

from subprocess import run, PIPE
from notify import notify
import os

UID = os.environ['uid']
DEV_NAME = os.environ['device_name']


def main():
    ret_val = unpair()
    call_notification(ret_val)


def call_notification(text_ind):
    out = [
        [f'Successfully unpaired {DEV_NAME}', 'Device permanently removed.'],
        [f'Failed to unpair {DEV_NAME}', 'Make sure you are connected to the device, and try again.']
    ]

    notify(out[text_ind][0], out[text_ind][1])


# Return    0   Successfully inpaired
#           1   Error
def unpair():
    # Turn off blueutooth if off
    if run('./blueutil --power'.split(), stdout=PIPE).returncode == 0:
        run('./blueutil --power 1; sleep 1'.split(), stdout=PIPE)

    # Try to unpair
    if run(f'./blueutil --unpair {UID}'.split(), stdout=PIPE).returncode == 0:
        return 0
    return 1


if __name__ == '__main__':
    main()
