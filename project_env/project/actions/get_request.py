# coding : utf-8
"""
Name of the file : get_request.py
Description : the script get_request will read and collect 
the request information from a access log file
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
__status__ = 'Get_request'


def requests_find(request_user, file_path):
    with open(file_path, "r") as fichier :
        request_tab = []
        for lignes in fichier :
            regex = r'^'+request_user #Start by the input user
            requestlo = re.search(r'([A-Z]* /[a-zA-Z/._-]*[ a-zA-Z.-_/0-9]*/?[0-9.]*)', lignes)#REGEX to get the request section
        #If the adresse ip is find   
            if(requestlo):
                start = re.search(regex, requestlo.group(1))#the variable start will get the input user and the matching request
            #finally if start is true let's print reponselo
                if(start):
                     request_tab.append(requestlo.group(0))
    return request_tab #return value
