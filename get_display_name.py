#!/usr/bin/python

from __future__ import print_function, absolute_import
from subprocess import check_output
import json
import sys

from return_device_json import get_display_name


def main():
	dev_id = sys.argv[1].decode("utf-8")
	dev_name = get_display_name(dev_id)
	if not dev_name:
		dev_info = check_output(["/usr/local/bin/blueutil", "--format", "json", "--info", dev_id])
		dev_name = json.load(dev_info)["name"]
	print(dev_name)

if __name__ == "__main__":
    main()