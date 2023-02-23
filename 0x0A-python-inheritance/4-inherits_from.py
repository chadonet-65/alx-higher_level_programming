#!/usr/bin/python3
# 4-inherits_from(.py
"""Defines a class function"""


def inherits_from(obj, a_class):
    """Check if an object is exactly an instance of given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Rteurns:
        If obj is exactly an instance of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
