#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name of the file : syslog_parser.py
Description : the script syslog_parser will read and collect 
the information from a syslog file
"""


#Import libraries needed for the script

import os
import re 
import sys 


__author__ = ''
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''


def get_month(month, file_path):
	"""
	return all the month in the syslog file
	"""
	list_month=[] # initialize empty list_month
	with open(file_path, 'r') as file:
		for lines in file:
			# Loop over lines of the "file" variable content and stock the regex in "month" variable
			# if "month" is not empty, then the "list_month" is incremented by the value
			regex = r'^'+month
			#month_re=re.search(r'^([A-Z]{1}[a-z]{2} )', lines)
			month_re=re.search(r'^([A-Z]{1}[a-z]{2})', lines)
			if month_re:
			#	list_month+=month.group(1)+'\n'
                        	start = re.search(regex, month_re.group(1))
	                	#if start:
                        	if start:
                        		list_month.append(month_re.group(0))
	return list_month


def get_day(day, file_path):
	list_day=[]
	with open(file_path, 'r') as file:
		for lines in file:
			regex = r'^ '+day
			#day_re=re.search(r'( {2}[0-9]{1} )', lines)
			day_re=re.search(r'( [0-9]{1,2} )', lines)
			if day_re:
                        	start = re.search(regex, day_re.group(1))
                        	if start:
                        		list_day.append(day_re.group(0).strip())
                        		#list_day.append(day_re.group(0)[2:])
				#list_day+=day.group(1)+'\n'
	return list_day


def get_hours(hours, file_path):
	list_hours=[]
	with open(file_path, 'r') as file:
		for lines in file:
			regex = r'^ '+hours
			#hours_re=re.search(r'(([0-9]{2}:){2}[0-9]{2} )', lines)
			hours_re=re.search(r'( ([0-9]{2}:){2}[0-9]{2} )', lines)
			if hours_re:
                        	start = re.search(regex, hours_re.group(1))
                        	if start:
                        		list_hours.append(hours_re.group(0).strip())
				#list_hours+=hours.group(1)+'\n'
	return list_hours

def get_infos(infos, file_path):
	list_infos=[]
	with open(file_path, 'r') as file:
		for lines in file:
			regex = r'^'+infos
			# infos_re=re.search(r'(: (([#(<\[])|[a-z]|[A-Z])[a-z].+)', lines)
			infos_re = re.search(r'(: .+)', lines)
			if infos_re:
                        	start = re.search(regex, infos_re.group(1)[2:])
                        	if start:
                        		list_infos.append(infos_re.group(0)[2:])
				#list_infos+=infos.group(1)[1:]+'\n' # [1:] remove the first caractere which is ':'
	return list_infos

def get_daemon(daemon, file_path):
	list_daemon=[]
	with open(file_path, 'r') as file:
		for lines in file:
			regex = r'^'+daemon
			# daemon_re=re.search(r'((([-./]|[A-Z]|[a-z])+[[0-9]{1,}]:|[a-z]{1,}:( |  )\[|nm-dispatcher:))', lines)
			daemon_re = re.search(r' ([a-zA-Z][^: ]*:)', lines)
			if daemon_re:
                        	start = re.search(regex, daemon_re.group(1)[:-1])
	                	#if start:
                        	if start:
                        		list_daemon.append(daemon_re.group(1)[:-1])
				#list_daemon+=daemon.group(1)[:-1]+'\n' # [:-1] remove the last caractere which is ':'
	return list_daemon

def get_computer_name(computer_name, file_path):
	list_computer_name=[]
	with open(file_path, 'r') as file:
		for lines in file:
			regex = r'^'+computer_name
			computer_name_re=re.search(r'(:[0-9]{2} [a-zA-Z0-9_-]{2,} )', lines)
			if computer_name_re:
                        	start = re.search(regex, computer_name_re.group(1)[4:-1])
	                	#if start:
                        	if start:
                        		list_computer_name.append(computer_name_re.group(0)[4:-1])
				#print('name -> ', computer_name.group(1)[3:]) # [3:] remove the three first caractere which is ':xx'
				#list_computer_name+=computer_name.group(1)[3:]+'\n'
	return list_computer_name



def filter_all_sys_log_fields(file_path, month, day, hour, computer_name, daemon,  message):
	result_list = []
	with open(file_path, 'r') as file:
		for line in file:
			line_list = []

			# month filtering
			regex = r'^' + month
			month_re = re.search(r'^([A-Z]{1}[a-z]{2})', line)
			if month_re:
				start = re.search(regex, month_re.group(1))
				if not start:
					continue
				line_list.append(month_re.group(0))

			# day filtering
			regex = r' ' + day
			day_re = re.search(r'( [0-9]{1,2} )', line)
			if day_re:
				start = re.search(regex, day_re.group(1))
				if not start:
					continue
				line_list.append(day_re.group(0).strip())

			# hour filtering
			regex = r' ' + hour
			hours_re = re.search(r'( ([0-9]{2}:){2}[0-9]{2} )', line)
			if hours_re:
				start = re.search(regex, hours_re.group(1))
				if not start:
					continue
				line_list.append(hours_re.group(0).strip())

			# computer_name filtering
			regex = r'^' + computer_name
			computer_name_re = re.search(r'(:[0-9]{2} [a-zA-Z0-9_-]{2,} )', line)
			if computer_name_re:
				start = re.search(regex, computer_name_re.group(1)[4:-1])
				if not start:
					continue
				line_list.append(computer_name_re.group(0)[4:-1])

			# daemon filtering
			regex = r'^' + daemon
			# daemon_re = re.search(r'((([-./]|[A-Z]|[a-z])+[[0-9]{1,}]:|[a-z]{1,}:( |  )\[|nm-dispatcher:))', line)
			daemon_re = re.search(r' ([a-zA-Z][^: ]*:)', line)
			if daemon_re:
				start = re.search(regex, daemon_re.group(1)[:-1])
				if not start:
					continue
				line_list.append(daemon_re.group(1)[:-1])

			# message filtering
			regex = r'^' + message
			# message_re = re.search(r'(: (([#(<\[])|[a-z]|[A-Z])[a-z].+)', line)
			message_re = re.search(r'(: .+)', line)
			if message_re:
				start = re.search(regex, message_re.group(1)[2:])
				if not start:
					continue
				line_list.append(message_re.group(0)[2:])

			result_list.append(line_list)

	return result_list

