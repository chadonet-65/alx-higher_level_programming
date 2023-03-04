#!/usr/bin/python3
"""
  3-to_json_string
  function to return json object
"""
import json


def from_json_string(my_str):
    """return json object"""
    return json.loads(my_str)
