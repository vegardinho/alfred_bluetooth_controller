#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function, absolute_import

import json
import os
from subprocess import check_output
import sys
import xml.etree.ElementTree as ET

# Workflow's cache directory for machine-specific data
CACHE_DIR = os.getenv("alfred_workflow_cache")
DEVICES_PATH = os.path.join(CACHE_DIR, "devices.json")


def main():
    """Run script."""
    # Script command
    subtitle = sys.argv[1].decode("utf-8")
    # User search query
    query = sys.argv[2].decode("utf-8") if len(sys.argv) > 2 else None

    # Ensure cache directory exists
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    if not query:  # Get devices from blueutil
        cmd_args = get_args(subtitle)
        js = check_output(cmd_args)
        with open(DEVICES_PATH, "w") as fp:
            fp.write(js)
        devices = json.loads(js)
    else:  # Read cached list of devices
        with open(DEVICES_PATH) as fp:
            devices = json.load(fp)

    # Generate Alfred feedback
    items = []
    for device in devices:
        device_name = device["name"]
        if device_name is None:
            continue        

        # Check if custom name
        display_name = get_display_name(device["address"])
        if display_name:
            device_name = display_name

        # Filter device name against user query if present
        if query and not query.lower() in device_name.lower():
            continue


            
        items.append(device_item(device_name, subtitle, device))

    if not items:
        items.append(
            dict(title="No Devices Found",
                subtitle = "Make sure the device is in search mode "
                                 "and within range, and try again"))

    json.dump({"items": items}, sys.stdout)


def get_display_name(address):
    try:
        xml = check_output("plutil -extract DeviceCache.{}.displayName xml1 /Library/Preferences/com.apple.Bluetooth.plist -o -".format(address).split())
    except Exception:
        return None
    return ET.fromstring(xml).find('string').text


def device_item(device_name, subtitle, device):
    """Return an Alfred feedback ``dict`` for device/message."""
    is_connected = device["connected"]
    d = dict(title=device_name,
             subtitle="Disconnect" if is_connected else "Connect",
             arg=device_name,
             autocomplete=device_name,
             icon=dict(path= "./icons/bt_icon_" + ("green" if is_connected else "blue") + ".png"))

    if device["address"]:
        d["uid"] = device["address"]
        d["variables"] = dict(uid=device["address"])

    return d


def get_args(subtitle):
    """Make ``blueutil`` command based on subtitle."""
    cmd_args = ["/usr/local/bin/blueutil", "--format", "json"]
    if subtitle == "Pair with device":
        cmd_args.extend(["--inquiry", "5"])
    else:
        cmd_args.extend(["--paired"])

    return cmd_args


if __name__ == "__main__":
    main()
