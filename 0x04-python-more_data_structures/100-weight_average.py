#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    if len(my_list) > 0:
        total = 0
        demon = 0
        d = dict(my_list)
        for i, item in d.items():
            total += int(i) * int(item)
            demon += int(item)
        result = total / demon

    return (result)
