#!/usr/bin/python

from __future__ import print_function, absolute_import
from subprocess import check_output
import json
import sys

def main():
	state = check_output(["/usr/local/bin/blueutil", "-p"]).rstrip()
	is_enabled = True if state == "1" else False
	item = dict(
		title = "Turn off bluetooth" if is_enabled else "Turn on bluetooth",
		subtitle = "Blueutooth currently " + ("enabled" if is_enabled else "disabled") + ".",
		icon = dict(path = "./icons/bt_icon_" + ("green" if is_enabled else "blue") + ".png")
	)
	json.dump({"items": [item]}, sys.stdout)




if __name__ == "__main__":
    main()