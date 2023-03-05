#!/usr/bin/python3
"""
  8-class_to_json.py
  function to return json object
"""


def class_to_json(obj):
    dic = {}
    if hasattr(obj, '__dict__'):
        dic = obj.__dict__.copy()
    return dic
