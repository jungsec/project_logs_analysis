# -*- coding: utf-8 -*-

"""
Name of the file : controller.py
Description : The aim of this file is to be the link between regex filter methods and the interface
"""

__author__ = 'koeman'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''


from actions.get_ip_adress import ip_find
from tkinter.constants import *


def find_filter_field(log_type_var, field_index, input_var, results_listbox, file_path):
    if log_type_var.get() == "Apache access log":
        if field_index == 0:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *ip_find(input_var.get(), file_path))