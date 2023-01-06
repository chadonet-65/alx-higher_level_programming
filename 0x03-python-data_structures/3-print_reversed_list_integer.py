#!/usr/bin/python3
# Author - tibaut

def print_reversed_list_integer(my_list=[]):
    for list in range(len(my_list)-1, -1, -1):
        print(my_list[list])
