#!/usr/bin/python3
"""
  1-write_file.py
  write a string to text
"""


def write_file(filename="", text=""):
    """function that print charater of file"""
    with open(filename, 'w', encoding='utf-8') as f:
        print(f.write(text))
