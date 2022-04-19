#!./python3
# encoding: utf-8

import subprocess
from sys import stdout

CMD = "perl -e 'use strict; use warnings; my $device =`security find-generic-password -w -s \"alfred-bluetooth-device-id\"`; chomp $device; print $device;'"

def main():
    stdout.write(get_fav_dev())

def get_fav_dev():
    fav_dev = subprocess.check_output(CMD, shell=True)
    return fav_dev.decode()

if __name__ == '__main__':
    main()
