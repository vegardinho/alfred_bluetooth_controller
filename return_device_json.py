#!/usr/bin/env python3

from subprocess import Popen, PIPE
import json
import sys

def main():
    subtitle = sys.argv[1]
    num_arg = len(sys.argv)


# Open pipe to bash, run command, read output, and convert json to list, if first call (no extra
# parameters). Read from file otherwise
    if num_arg == 2:
        cmd_args = get_args(subtitle)
        p = Popen(cmd_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        text_json = output.decode('utf-8')
        open("devices.json", "w").write(text_json)
        devices = json.loads(text_json)
    else:
        devices = json.loads(open("devices.json", "r").read())

    # print(devices)

# Create json manually from content in list (and argument), and print to alfred
    items = """{"items": ["""
    items_len = len(items)

    for device in devices:
        device_name = device['name']
        if (device_name == None):
            continue
        
        if num_arg > 2:
            match = check_if_match(num_arg, device_name)
            if match == False:
                continue

        items += to_json_str(device_name, subtitle, device['address'])


    if items_len == len(items):
        items += to_json_str("No Devices Found", "Make sure the device is in search mode and within range, and try again", "")
    items = items[:-1] + "]}"""

    print(items)

def to_json_str(device_name, sub_text, device_id):
    name_lower = device_name.lower()
    name = device_name
    dev_id = device_id
    sub = sub_text

    string = "{" + """
                    "uid": "{}",
                    "title": "{}",
                    "subtitle": "{}",
                    "arg": "{}",
                    "autocomplete": "{}\"""".format(name_lower, name, sub, name, name) + "},"
    return string

def get_args(sub):
    subtitle = sub

    cmd_args = ["/usr/local/bin/blueutil"]
    if subtitle == "Pair with device":
        cmd_args.extend(["--inquiry", "3"])
    else:
        cmd_args.extend(["--paired"])
    cmd_args.extend(["--format", "json"])

    return cmd_args

def check_if_match(num_arg, device_name):
    for i in range(2, num_arg):
        if (sys.argv[i].lower() not in device_name.lower()):
            return False
    return True

main()
