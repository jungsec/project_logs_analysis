#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name of the file : read_file.py
Description : The aim of this file is to read any log file
call read_log_file() for testing
"""

import sys

__author__ = 'jungsec'
__copyright__ = ''
__credits__ = ['jungsec']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = 'jungsec'
__email__ = ''
__status__ = 'Prototype'


def read_log_file(log_file=sys.argv[1]):
    """
    This function take for argument the log file and read it
    """
    with open(log_file) as log_file:
        read_log_file = log_file.read()
    return read_log_file
