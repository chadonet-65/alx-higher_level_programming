#!/usr/python3

def roman_to_int(roman_string):
    result = 0
    if type(roman_string) == str and roman_string is not None:
        string = roman_string
        strlen = len(string)
        std = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(strlen):
            if (i > 0) and (std[string[i]] > std[string[i - 1]]):
                result += int(std[string[i]]) - int(std[string[i - 1]]) * 2
            else:
                result += std[string[i]]
    return result
