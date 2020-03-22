from subprocess import Popen, PIPE
import json
import sys

# Open pipe to bash, run command, read output, and convert json to list.
p = Popen(["/usr/local/bin/blueutil", "--paired", "--format" ,"json"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
devices = json.loads(output.decode('utf-8'))

subtitle = sys.argv[1]

# Create json manually from content in list (and argument), and print to alfred
items = """{"items": ["""

for device in devices:
    device_name = device['name']
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
