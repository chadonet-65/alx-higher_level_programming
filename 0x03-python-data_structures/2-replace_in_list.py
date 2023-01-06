#!/usr/bin/python3
# Author - tibaut

def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx > x:
        print(my_list)
    elif idx < 0:
        print(my_list)
    else:
        my_list[idx] = element
        print(my_list)
