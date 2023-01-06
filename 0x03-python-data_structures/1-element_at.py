#!/usr/bin/python3
# Author - tibaut

def element_at(my_list, idx):
    x = len(my_list)
    if idx > x:
        return 0
    elif idx < 0:
        return 0
    else:
        print("Elemet at index {:d} is {}".format(idx, my_list[idx]))
