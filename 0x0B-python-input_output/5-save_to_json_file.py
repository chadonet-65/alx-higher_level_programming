#!/usr/bin/python3
"""
  5-to_json_string
  function to return json object
"""
import json


def save_to_json_file(my_obj, filename):
    """return json object"""
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
