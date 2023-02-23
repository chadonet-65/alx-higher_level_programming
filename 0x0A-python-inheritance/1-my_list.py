#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyList"""


class MyList(list):
    """Implement sorted printing"""

    def print_sorted(self):
        """Print a list in sorted ascending"""
        print(sorted(self))
