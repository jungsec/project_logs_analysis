# coding : utf-8
"""
Name of the file : get_ip_adress.py
Description : the script get_ip_adress will read and collect 
the all the ip adress from a log file
"""


#Import libraries needed for the script

import re

__author__ = 'GMEddy'
__copyright__ = ''
__credits__ = ['GMEddy']
__licence__ = ''
__version__ = '0.0.1'
__maintainer__ = 'GMEddy'
__email__ = ''
__status__ = 'Get_ip_log'


def ip_find(ip_user, file_path):
    with open(file_path, "r") as fichier :
        ip_tab = []
        for lignes in fichier :
            regex = r'^'+ip_user #Start by the input user
            ip_adresslo = re.search(r'(([0-9\.]+[0-9\.]+[0-9\.]+[0-9]+))', lignes)#regex for all the IP in the file 
        #If the adresse ip is find   
            if(ip_adresslo):
                start = re.search(regex, ip_adresslo.group(1))#the variable start will get the input user and the matching ip adress
            #finally if start is true let's print ip_adresslo
                if(start):
                    ip_tab.append(ip_adresslo.group(0))
                    #print ("adresse ip :",ip_adresslo.group(0))
    return ip_tab #return value
