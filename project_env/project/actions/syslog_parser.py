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


__author__ = 'jungsec'
__copyright__ = ''
__credits__ = ['']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = ''
__email__ = ''
__status__ = ''


def get_month():
        """
        return all the month in the syslog file
        """
        list_month='' # initialize empty list_month
        with open('syslog_test', 'r') as file:
                for lines in file:
                        # Loop over lines of the "file" variable content and stock the regex in "month" variable
                        # if "month" is not empty, then the "list_month" is incremented by the value
                        month=re.search(r'^([A-Z]{1}[a-z]{2} )', lines)
                        if month:
                                list_month+=month.group(1)+'\n'
                        else:
                                print('nothin')
        return list_month


def get_day():
        list_day=''
        with open('syslog_test', 'r') as file:
                for lines in file:
                        day=re.search(r'( {2}[0-9]{1} )', lines)
                        if day:
                                list_day+=day.group(1)+'\n'
                        else:
                                print('dont work')
        return list_day

def get_hours():
        list_hours=''
        with open('syslog_test', 'r') as file:
                for lines in file:
                        hours=re.search(r'(([0-9]{2}:){2}[0-9]{2} )', lines)
                        if hours:
                                list_hours+=hours.group(1)+'\n'
                        else:
                                print('dont work too')
        return list_hours

def get_infos():
        list_infos=''
        with open('syslog_test', 'r') as file:
                for lines in file:
                        infos=re.search(r'(: (([#(<\[])|[a-z]|[A-Z])[a-z].+)', lines)
                        if infos:
                                list_infos+=infos.group(1)[1:]+'\n' # [1:] remove the first caractere which is ':'
                        else:
                                print('dont work ')
        return list_infos

def get_daemon():
        list_daemon=''
        with open('syslog_test', 'r') as file:
                for lines in file:
                        daemon=re.search(r'((([-./]|[A-Z]|[a-z])+[[0-9]{1,}]:|[a-z]{1,}:( |  )\[|nm-dispatcher:))', lines)
                        if daemon:
                                list_daemon+=daemon.group(1)[:-1]+'\n' # [:-1] remove the last caractere which is ':'
                        else:
                                print('dont work ')
        return list_daemon

def get_computer_name():
        list_computer_name=''
        with open('syslog_test', 'r') as file:
                for lines in file:
                        computer_name=re.search(r'(:[0-9]{2} [a-zA-Z0-9_-]{2,} )', lines)
                        if computer_name:
                                #print('name -> ', computer_name.group(1)[3:]) # [3:] remove the three first caractere which is ':xx'
                                list_computer_name+=computer_name.group(1)[3:]+'\n'
                        else:
                                print('dont work ')
        return list_computer_name

print(get_month())
print(get_day())
print(get_hours())
print(get_infos())
print(get_daemon())
print(get_computer_name())
