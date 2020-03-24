#!/usr/bin/env python3

from subprocess import Popen, PIPE
import json
import sys

def main():
    subtitle = sys.argv[1]
    num_arg = len(sys.argv)

    if num_arg == 2:
# Open pipe to bash, run command, read output, and convert json to list.
        p = Popen(["/usr/local/bin/blueutil", "--paired", "--format" ,"json"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        text_json = output.decode('utf-8')
        open("devices.json", "w").write(text_json)
        devices = json.loads(text_json)
    else:
        devices = json.loads(open("devices.json", "r").read())

# Create json manually from content in list (and argument), and print to alfred
    items = """{"items": ["""

    for device in devices:
        device_name = device['name']
        if (device_name == None):
            continue
        
        if num_arg > 2:
            match = check_if_match(num_arg, device_name)
            if match == False:
                continue

        items += ("{" + """
                    "uid": "{}",
                    "title": "{}",
                    "subtitle": "{}",
                    "arg": "{}",
                    "autocomplete": "{}\""""
                    .format(device_name.lower(), device_name, subtitle, 
                        device['address'], device_name) + "},")

    items = items[:-1] + "]}"

    print(items)

def check_if_match(num_arg, device_name):
    for i in range(2, num_arg):
        if (sys.argv[i].lower() not in device_name.lower()):
            return False
    return True

main()
