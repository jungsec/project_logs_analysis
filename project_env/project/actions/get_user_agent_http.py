# coding : utf-8
"""
Name of the file : get_request.py
Description : the script get_user_agent will read and collect 
the user agent information from a access log file
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
__status__ = 'Get_user_agent_http'

def user_agent_find(agent_user, file_path):
    with open(file_path, "r") as fichier :
        user_tab = []
        for lignes in fichier :
            regex = r'^'+agent_user #Start by the input user
            user_agentlo = re.search(r'("[A-Za-z]+/[0-9;/.()A-Za-z -]+)', lignes)#REGEX to get the user agent navigator ect
        #If the adresse ip is find   
            if(user_agentlo):
                start = re.search(regex, user_agentlo.group(1))#the variable start will get the input user and the matching user agent
            #finally if start is true let's print reponselo
                if(start):
                     user_tab.append(user_agentlo.group(0))
    return user_tab #return value
