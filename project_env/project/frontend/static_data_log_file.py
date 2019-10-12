#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name of the file : tab_syslog.py
Description : the script tab_syslog will read and collect 
the static information from a syslog file
"""


#Import libraries needed for the script

import os
import re
import sys


__author__ = 'jungsec,koeman'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''

def number_of_line(log_file_name):
	"""
	Get the total lines of log file

	Parameters
   	----------
    	log_file_name : str
		The name of the log file

	Returns
	----------
	total_lines : str
		The total line of the log file
	"""
	print(log_file_name)
	log_file = open(log_file_name, 'r')
	total_lines = 0
	for line in log_file:
		total_lines += 1
	return total_lines 

def name_file(log_file_path):
	"""
	Get the name of log file in both linux and windows os

	Parameters
   	----------
    	log_file_path : str
		The path of the log file

	Returns
	----------
	log_file_path.split('/')[-1] : str
		The last attribute of the path, so the name of the file
	log_file_path.split('\\')[-1] : str
		The last attribute of the path, so the name of the file
	"""

	if sys.platform.startswith('lin') or sys.platform.startswith('dar'):
		return log_file_path.split('/')[-1]
	if sys.platform.startwith('win') or sys.platform.startswith('cyg'):
		return log_file_path.split('\\')[-1]
	
	print('os unknown')
