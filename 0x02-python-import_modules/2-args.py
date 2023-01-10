#!/usr/bin/python3
from sys import argv

def dynamic(arr):
    tabLen = len(arr)
    if tabLen == 0:
        print("0 argument")
    elif tabLen == 1:
        print("1 argument:\n1",arr[0])
    else:
        print("{} arguments:".format(tabLen))
        for (i, item) in enumerate(arr, start=1)):
            print(f"{i}: {item}")

if (__name__ == '__main__'):
    dynamic(argv[1:])
