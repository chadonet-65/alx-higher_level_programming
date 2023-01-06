#!/usr/bin/python3
# Author - tibaut

def no_c(my_string):
    for string in my_string:
        if string != 'c' and string != 'C':
            print(string)
