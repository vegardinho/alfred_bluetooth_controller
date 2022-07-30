#!/usr/bin/python3
# encoding: utf-8

import json
import sys


def script_output(**kwargs):
    alfredworkflow = {"arg": "https://www.google.com", "variables": dict(kwargs)}
    json.dump({"alfredworkflow": alfredworkflow}, sys.stdout)
