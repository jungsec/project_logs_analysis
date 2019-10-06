# coding : utf-8
"""
Name of the file : access_log_parser.py
Description : the script access_log_parser will read and collect 
the information from a access log file
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
__status__ = 'Get_access_log'

"""
The form of the acces log file is :
LogFormat "%h %l %u %t \"%r\" %>s %b" common
CustomLog logs/access_log commo
IP adress - frank [day/mounth/year:hour:minutes:secondes zone] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)" 

"""
"""
#using awk fonction 
with open('/home/eddy/Bureau/Projet_python/project_logs_analysis/project_env/project/actions/test_access.log',"r") as f :

    for lines in f:
        fields = lines.strip("\n").split(" ")
        # the seconde and third is not interresting lets focus on the rest 
        a = fields[0]
        #b = fields[1:3]
        ip_adresslo = re.search(r'^([0-9\.]+)', lines)

        if ip_adresslo : 
            print(f"{a}")

        else :
            print("nope")
"""
#grep version 

with open("","r") as fichier : 
    for lignes in fichier : 
        #109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
        ip_adresslo = re.search(r'^([0-9\.]+)', lignes)
        timelo = re.search(r'([[0-9A-Za-z/]+[:0-9]+ [+0-9]+)', lignes)
        requestlo = re.search(r'([A-Z]* /[a-zA-Z/._-]*[ a-zA-Z.-_/0-9]*/?[0-9.]*)', lignes)
        reponselo = re.search(r'([0-9]+ [0-9]+)', lignes)
        navlo = re.search(r'("[A-Za-z]+/[0-9;/.()A-Za-z -]+)', lignes)
        if ip_adresslo and timelo :  
           print("Adresse IP : ",ip_adresslo.group(1), "date access :",timelo.group(1))
           #print("Date access: ",timelo.group(1))
        #if requestlo and reponselo :
         #   print ("request :" , requestlo.group(1))
          #  print ("reponse :" , reponselo.group(1))

        #if navlo :
              #print ("navigation :" , navlo.group(1))
        else:
            print("pas de donnée ")

"""
Write a funstion who will return "lignes" and after "lignes" will be use as object in the other fonction 
to collect the information needed 
"""


        