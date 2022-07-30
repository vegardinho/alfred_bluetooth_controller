#!/usr/bin/python3
# encoding: utf-8

import subprocess


CMD = "perl -e 'use strict; use warnings; my $device =`security find-generic-password -w -s " \
      "\"alfred-bluetooth-device-id\"`; chomp $device; print $device;' "

def get_fav_dev():
    try:
        fav_dev = subprocess.check_output(CMD, shell=True)
    except subprocess.CalledProcessError:
        return

    return fav_dev.decode()