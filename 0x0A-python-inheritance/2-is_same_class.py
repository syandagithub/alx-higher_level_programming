#!/usr/bin/python3
# 2-is_same_class.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a class-checking function."""


def is_same_class(obj, a_class):

    if type(obj) == a_class:
        return True
    return False
