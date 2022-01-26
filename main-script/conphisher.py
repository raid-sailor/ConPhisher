#!/usr/bin/env python

import sys
import requests
import json
import os 
from colorama import Fore, Back, Style
import socket
from cymruwhois import Client
from pyfiglet import *
import getopt
import argparse

custom_fig = Figlet(font='graffiti')

author =  Figlet(font='graceful')

parser = argparse.ArgumentParser()

parser.add_argument('-e', action='store', dest='email',
                    help='Your email address')

parser.add_argument('-u', action='store', dest='url',
                 
                    help='Target url')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

print(results.url)
def netcraft_post():

        try:

            r = requests.post('https://report.netcraft.com/api/v3/report/urls', json={
            "email": results.email,
            "urls": [{ "url": "https://" + results.url, "country": "GB" }],
            })

            print(Fore.BLUE + "Netcraft" + Style.RESET_ALL)
            print( "\nReported to Netcraft as a malicious with takedown ID: " + r.json()['uuid'] )
        except KeyError:
            print("\nError! Make sure you entered your email otherwise try again later.")
            pass
        

def enumeration(): 

    print(Fore.BLUE + "Target Enumeration\n" + Style.RESET_ALL)
    os.system('gobuster dir -q -u' + results.url + '/ -w wordlist.txt -r')

def whois_ip():
    try: 

        domainip = socket.gethostbyname(results.url)
        c = Client()
        r = c.lookup(domainip)
        print(Fore.BLUE + "Site Information\n" + Style.RESET_ALL)
        print("ASN: " + r.asn)
        print("ASN Owner: " + r.owner)
        print("Host IP: " + r.ip)
    except TypeError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nNO URL PROVIDED.\n")
            sys.exit()
 
while True:     
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(results.url + results.email)
    print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
    print(Fore.CYAN + ("❌ This tool is not intended for malicious purposes ❌") + Style.RESET_ALL)
    print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
    menu_input = input("\nThis will report the site for a takedown with Netcraft. Do you want to continue? ") 

    if menu_input == "Yes" or menu_input == "yes": 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
        print(Fore.CYAN + ("❌ This tool is not intended for malicious purposes ❌") + Style.RESET_ALL)
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



