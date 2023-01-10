#!/usr/bin/python3
from sys import argv

def add(arr):
    if len(arr) == 0:
        print("0")
    else:
        total = 0
        for i in range(0, len(arr)):
            total += int(arr[i])

        print(total)

if __name__=='__main__':
    add(argv[1:])
