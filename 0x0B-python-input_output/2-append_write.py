#!/usr/bin/python3
"""
  1-write_file.py
  write a string to text
"""


def append_write(filename="", text=""):
    """ function that appends a string returns the number of characters """ 
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
