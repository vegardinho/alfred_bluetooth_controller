#!/usr/bin/python3
# encoding: utf-8

from subprocess import run


def notify(title, message, subtitle='', sound='Frog'):
    cmd = ['./notificator', '--title', title, '--message', message, '--sound', sound]

    if subtitle != '':
        cmd.append('--subtitle')
        cmd.append(subtitle)

    run(cmd)

