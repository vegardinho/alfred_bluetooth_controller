#!/usr/bin/python3

from subprocess import check_output
import json
import sys
import xml.etree.ElementTree as ET


def get_display_name(dev_id):
	dev_name = get_custom_name(dev_id)
	if not dev_name:
		dev_info = check_output(["blueutil", "--format", "json", "--info", dev_id])
		dev_name = json.loads(dev_info)["name"]
	return dev_name


def get_custom_name(address):
	"""Check cache file for custom file name"""
	try:
		plist_cmd = "plutil -extract DeviceCache.{}.displayName xml1 /Library/Preferences/com.apple.Bluetooth.plist -o -".format(address)
		xml = check_output(plist_cmd.split())
	except Exception as e:
		return None
	return ET.fromstring(xml).find('string').text


if __name__ == "__main__":
	get_display_name(sys.argv[1])
