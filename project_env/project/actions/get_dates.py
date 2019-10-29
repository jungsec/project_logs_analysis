# coding : utf-8
"""
Name of the file : get_dates.py
Description : the script get_dates will read and collect 
the all the dates from a log file
"""


#Import libraries needed for the script

#import argparse
import os
import re 
import sys 


__author__ = 'GMEddy'
__copyright__ = ''
__credits__ = ['GMEddy']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = 'GMEddy'
__email__ = ''
__status__ = 'Get_date'

#create a function for the dates in log file
#befor we need to show the format of the date for the user 
 
def dates_find(date_user, file_path):#date user 
    with open(file_path, "r") as fichier :
        dates_tab = []
        for lignes in fichier :
            regex = r'^\['+date_user
            date_user #Start by the input user
            timelo = re.search(r'([[0-9A-Za-z/]+[:0-9]+ [+0-9]+])', lignes)#REGEX to get the date and time section
        #if the time is find   
            if(timelo):
                start = re.search(regex, timelo.group(1))#the variable start will get the input user and the matching ip adress
            #finally if start is true let's print the time 
                if(start):
                    dates_tab.append(timelo.group(0))
    return dates_tab #return value