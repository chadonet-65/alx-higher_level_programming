#!/usr/bin/python3
# Author - tibaut

def replace_in_list(my_list, idx, element):
    if idx > len(my_list) - 1 or idx < 0:
        return 'None'
    else:
        my_list[idx] = element
        return my_list
