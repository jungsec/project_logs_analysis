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

#using awk fonction to get only the section we want 
"""with open('/PATH/',"r") as f :

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
"""
with open("/PATH/","r") as fichier : 
    for lignes in fichier : 
        #109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
        ip_adresslo = re.search(r'^([0-9\.]+)', lignes) #REGEX to get the IP adress section
        timelo = re.search(r'([[0-9A-Za-z/]+[:0-9]+ [+0-9]+)', lignes)#REGEX to get the date and time section
        requestlo = re.search(r'([A-Z]* /[a-zA-Z/._-]*[ a-zA-Z.-_/0-9]*/?[0-9.]*)', lignes)#REGEX to get the request section
        reponselo = re.search(r'([0-9]+ [0-9]+)', lignes)#REGEX to get the reponse and package section
        navlo = re.search(r'("[A-Za-z]+/[0-9;/.()A-Za-z -]+)', lignes)#REGEX to get the navigator ect
        if ip_adresslo and timelo and requestlo and reponselo  : #if condition for each parameters  
           print("Adresse IP : ",ip_adresslo.group(1),"Date access :",timelo.group(1),"request :" , requestlo.group(1),"reponse :" , reponselo.group(1)) #show parameters matching  
        #if navlo :
              #print ("navigation :" , navlo.group(1))
        else:
            print("pas de donnée ")#no match
        
"""

"""
Next time lets combined tab and regex to show only what we need 
"""

"""
Write a function who will return "lignes" and after "lignes" will be use as object in the other fonction 
to collect the information needed 
"""

def collectInfo():
    with open("") as fichier : 
        ip_adresses = []
        dates_times = []
        requests = []
        reponses = []
        navigation = []

        for lignes in fichier : 
        #109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
            ip_adresslo = re.findall(r'^([0-9\.]+)', lignes) #REGEX to get the IP adress section findall
            #if ip_adresslo:
             #   ip_adresslo = ip_adresslo.group(1)
                #print(ip_adresslo)
            ip_adresses += ip_adresslo 
            
            timelo = re.findall(r'([[0-9A-Za-z/]+[:0-9]+ [+0-9]+)', lignes)#REGEX to get the date and time section
            dates_times += timelo
            
            requestlo = re.findall(r'([A-Z]* /[a-zA-Z/._-]*[ a-zA-Z.-_/0-9]*/?[0-9.]*)', lignes)#REGEX to get the request section
            
            requests += requestlo
            
            reponselo = re.findall(r'([0-9]+ [0-9]+)', lignes)#REGEX to get the reponse and package section
            reponses += reponselo

            navlo = re.findall(r'("[A-Za-z]+/[0-9;/.()A-Za-z -]+)', lignes)#REGEX to get the navigator ect
            navigation += navlo

            #if ip_adresslo :# and timelo and requestlo and reponselo  : #if condition for each parameters  
                 #print("Adresse IP : ",ip_adresslo.group(1))#,"Date access :",timelo.group(1),"request :" , requestlo.group(1),"reponse :" , reponselo.group(1)) #show parameters matching  
            #if navlo :
                #print ("navigation :" , navlo.group(1))
            #else:
                #print("pas de donnée ")#no match
    return ip_adresses,dates_times,requests,reponses,navigation,

print(collectInfo()[:])

#récuperer la fonction collectInfo dans le scripte IHM pour récuperer les champs nécéssaire 