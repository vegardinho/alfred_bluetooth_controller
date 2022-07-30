#!/usr/bin/python3
# encoding: utf-8

import subprocess
import os
from script_output import script_output
from get_display_name import get_display_name

CMD = "perl -e 'use strict; use warnings; my $device =`security find-generic-password -w -s " \
      "\"alfred-bluetooth-device-id\"`; chomp $device; print $device;' "


def main():
    uid = get_fav_dev()
    if not uid:
        notify_failure()
        return
    dev_name = get_display_name(uid)

    store_variables(0, dev_name, uid)


def notify_failure():
    title_vars = [
            'Bluetooth device not set',
            'It appears that device has not been set. Please run \'btset\' command and try again.'
        ]

    vars = {'not_title': title_vars[0], 'not_subtitle': title_vars[1],
            'uid': uid, 'device_name': dev_name}

    # Combine all variable names and variable keys
    script_output(**vars)

def get_fav_dev():
    try:
        fav_dev = subprocess.check_output(CMD, shell=True)
    except subprocess.CalledProcessError:
        return

    return fav_dev.decode()


if __name__ == '__main__':
    main()
