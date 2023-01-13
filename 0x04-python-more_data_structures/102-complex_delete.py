#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dict1 = dict(a_dictionary)
    for idx, item in dict1.items():
        del a_dictionary[idx]
    return (a_dictionary)
