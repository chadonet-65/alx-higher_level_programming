#!/usr/bin/python3
"""
  6-load_from_json_file.py
  function that create object json
"""
import json



def load_from_json_file(filename):
    """create a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
