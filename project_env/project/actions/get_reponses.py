# coding : utf-8
"""
Name of the file : get_request.py
Description : the script get_reponses will read and collect 
the reponses information from a access log file
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
__status__ = 'Get_reponses'


def reponses_find(reponse_user, file_path):
    with open(file_path, "r") as fichier :
        reponses_tab = []
        for lignes in fichier :
            regex = r'^'+reponse_user #Start by the input user
            reponselo = re.search(r'([0-9]+ [0-9]+)', lignes)#REGEX to get the reponse and package section
        #If the adresse ip is find   
            if(reponselo):
                start = re.search(regex, reponselo .group(1))#the variable start will get the input user and the matching reponse
            #finally if start is true let's print reponselo
                if(start):
                     reponses_tab.append(reponselo.group(0))
    return reponses_tab #return value

