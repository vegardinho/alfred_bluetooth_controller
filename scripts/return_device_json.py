#!/usr/bin/python3
# encoding: utf-8

import json
import os
from subprocess import check_output
import sys

import get_favorite
from get_display_name import get_custom_name

# Workflow's cache directory for machine-specific data
CACHE_DIR = os.getenv("alfred_workflow_cache")
DEVICES_PATH = os.path.join(CACHE_DIR, "devices.json")

FAV_DEV_ID = get_favorite.get_fav_dev()

def main():

    """Run script."""
    # Script command
    subtitle = sys.argv[1]
    # User search query
    query = sys.argv[2] if len(sys.argv) > 2 else None

    # Ensure cache directory exists
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)


    if not query:  # Get devices from blueutil
        cmd_args = get_args(subtitle)
        js_bytes = check_output(cmd_args)
        js = js_bytes.decode()
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
        display_name = get_custom_name(device["address"])
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





def device_item(device_name, subtitle, device):
    """Return an Alfred feedback ``dict`` for device/message."""
    is_connected = device["connected"]
    if subtitle == "Set as favorite":
        if device["address"] == FAV_DEV_ID:
            subtitle = "Current favorite"
        else:
            subtitle = "Set as favorite"
    elif subtitle != "Unpair":
        subtitle = "Disconnect" if is_connected else "Connect"

    d = dict(title=device_name,
             arg=device_name,
             subtitle=subtitle,
             autocomplete=device_name,
             variables=dict(device_name=device_name),
             icon=dict(path= "./icons/bt_icon_" + ("green" if is_connected else "blue") + ".png"))

    if device["address"]:
        d["uid"] = device["address"]
        d["variables"]["uid"] = device["address"]
    return d


def get_args(subtitle):
    """Make ``blueutil`` command based on subtitle."""
    cmd_args = ["./blueutil", "--format", "json"]
    if subtitle == "Pair with device":
        cmd_args.extend(["--inquiry", "5"])
    else:
        cmd_args.extend(["--paired"])

    return cmd_args


if __name__ == "__main__":
    main()
