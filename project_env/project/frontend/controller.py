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


from actions.get_dates import dates_find
from actions.get_request import requests_find
from actions.get_reponses import reponses_find
from actions.get_user_agent_http import user_agent_find
from actions.get_ip_adress import ip_find
from actions.syslog_parser import *
from tkinter.constants import *


def find_filter_field(log_type_var, field_index, input_var, results_listbox, file_path):
    if not file_path: return
    results_listbox.delete(0, END)
    
    if log_type_var.get() == "Apache access log":
        
        if field_index == 0:
            results_listbox.insert(0, *ip_find(input_var.get(), file_path))
        
        if field_index == 1:
            results_listbox.insert(0, *dates_find(input_var.get(), file_path))
        
        if field_index == 2:
            results_listbox.insert(0, *requests_find(input_var.get(), file_path))
            
        if field_index == 3:
            results_listbox.insert(0, *reponses_find(input_var.get(), file_path))
            
        if field_index == 4:
            results_listbox.insert(0, *user_agent_find(input_var.get(), file_path))

    if log_type_var.get() == "Linux Syslog":

        if field_index == 0:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_month(input_var.get(), file_path))

        if field_index == 1:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_day(input_var.get(), file_path))

        if field_index == 2:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_hours(input_var.get(), file_path))

        if field_index == 3:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_computer_name(input_var.get(), file_path))

        if field_index == 4:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_daemon(input_var.get(), file_path))

        if field_index == 5:
            results_listbox.delete(0, END)
            results_listbox.insert(0, *get_infos(input_var.get(), file_path))