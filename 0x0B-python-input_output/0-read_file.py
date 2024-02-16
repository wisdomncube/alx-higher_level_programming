#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:26:45
@author: Wisdom Ncube
"""

def read_file(filename=""):
    """
    Reads the file
    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
