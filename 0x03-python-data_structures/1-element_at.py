#!/usr/bin/python3
# Author - tibaut

def element_at(my_list, idx):
    x = len(my_list) - 1
    if idx > x or idx < 0:
        return 'None'
    else:
        return my_list[idx]
