#!/usr/bin/env python

import sys
import requests
import json
import os 
from art import *
from colorama import Fore, Back, Style
import whois
import socket
from cymruwhois import Client
from pyfiglet import *


phishing_url = sys.argv[1] 
Art=text2art( "") 
custom_fig = Figlet(font='graffiti')
author =  Figlet(font='graceful')

try:
    netcraft_api = sys.argv[2] 
except IndexError:
    netcraft_api = 'null'

def netcraft_post():

    if netcraft_api != 'null': 

        r = requests.post('https://report.netcraft.com/api/v3/test/report/urls', json={
        "email": netcraft_api,
        "urls": [{ "url": phishing_url, "country": "GB" }],
            })
        print(Fore.BLUE + "Netcraft" + Style.RESET_ALL)
        print( "\nReported to Netcraft as an malicious url with ID: " + r.json()['uuid'])

    else:
        print( "\nUnable to report to Netcraft due to no email address being provided")
    
def enumeration(): 
    print(Fore.BLUE + "Target Enumeration\n" + Style.RESET_ALL)
    os.system('gobuster dir -q -u' + phishing_url + '/ -w wordlist.txt -r')

def whois_ip():
    domainip = socket.gethostbyname(phishing_url)
    c = Client()
    r = c.lookup(domainip)
    print(Fore.BLUE + "Site Information" + Style.RESET_ALL)
    print("ASN: " + r.asn)
    print("ASN Owner: " + r.owner)
    print("Host IP: " + r.ip)
 

while True: 

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
    print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
    menu_input = input("\nThis will report the site for a takedown with Netcraft. Do you want to continue? ") 

    if menu_input == "Yes" or menu_input == "yes": 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
        print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
        print("\n====================================================\n")
        whois_ip()
        print("\n====================================================\n")
        netcraft_post()
        print("\n====================================================\n")
        enumeration()
        sys.exit()
    elif menu_input == "No" or menu_input == "no": 
        sys.exit()
    else: 
        input("\nIncorrect option picked, press enter to try again.")



