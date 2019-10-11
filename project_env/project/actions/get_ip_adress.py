# coding : utf-8
"""
Name of the file : get_ip_adress.py
Description : the script get_ip_adress will read and collect 
the all the ip adress from a log file
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
__status__ = 'Get_ip_log'

ip_user = (input("entrez votre ip :"))#variable use for the user ip 
a = "" #variable to stock the input 

def ip_find():
    with open("","r") as fichier : 
        ip_tab = []
        for lignes in fichier : 
            a = ip_user#stock input into {a}
         #109.169.248.247 
            regex = r'^'+a #Start by the input user
            ip_adresslo = re.search(r'(([0-9\.]+[0-9\.]+[0-9\.]+[0-9]+))', lignes)#regex for all the IP in the file 
        #If the adresse ip is find   
            if(ip_adresslo):
                start = re.search(regex, ip_adresslo.group(1))#the variable start will get the input user and the matching ip adress
            #finally if start is true let's print ip_adresslo
                if(start):
                    ip_tab.append(ip_adresslo.group(0))
                    #print ("adresse ip :",ip_adresslo.group(0))
    return ip_tab,#return value  

print(ip_find()[0])#print matching ip
       
"""
ip_user = (input("entrez votre ip :"))#variable use for the user ip 
a = "" #variable to stock the input 

with open("","r") as fichier : 
    for lignes in fichier : 
        a = ip_user#stock input into {a}
         #109.169.248.247 
        regex = r'^'+a #Start by the input user 
        ip_adresslo = re.search(r'(([0-9\.]+[0-9\.]+[0-9\.]+[0-9]+))', lignes)#regex for all the IP in the file 
        #If the adresse ip is find   
        if(ip_adresslo):
            start = re.search(regex, ip_adresslo.group(1))#the variable start will get the input user and the matching ip adress
            #finally if start is true let's print ip_adresslo
            if(start):
                ip_tab.append(ip_adresslo.group(0))
               print ("adresse ip :",ip_adresslo.group(0))        # print group 0
        
        #tab_ip = ip_adresslo + tab 
        #tab_recap = tab + tab_ip
        #if ip_adresslo :
         #   print ("adresse ip :",ip_adresslo.group(0))
        #else :
         #   print("no data")
return ip_tab         
"""

