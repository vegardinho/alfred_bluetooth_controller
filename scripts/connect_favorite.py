#!/usr/bin/python3
# encoding: utf-8

from notify import notify
from get_display_name import get_display_name
from connect import connect
import os
import get_favorite


def main():
    uid = get_favorite.get_fav_dev()
    if not uid:
        notify_failure()
        return

    dev_name = get_display_name(uid)

    os.environ['uid'] = uid
    os.environ['device_name'] = dev_name

    connect(uid, dev_name)



def notify_failure():
    title = 'Bluetooth device not set'
    subtitle = 'It appears that device has not been set. Please run \'btset\' command and try again.'

    notify(title, subtitle)


if __name__ == '__main__':
    main()
