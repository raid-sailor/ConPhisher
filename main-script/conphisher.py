#!/usr/bin/env python

import sys
import requests
import os 
from colorama import Fore, Style
import socket
from cymruwhois import Client
from pyfiglet import *
import argparse

custom_fig = Figlet(font='graffiti')
author =  Figlet(font='graceful')
parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='url',
                 
                    help='Target url')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()

def cookie_check():

        print(Fore.BLUE + "Observables\n" + Style.RESET_ALL)

        try:
            a_session = requests.Session()
            a_session.get('https://' + results.url)
            session_cookies = a_session.cookies
            cookies_dictionary = session_cookies.get_dict()
            print(cookies_dictionary)

        except requests.exceptions.ConnectionError:
            print("Cookie: Cookie details could not be processed.")

        except TypeError:
            print("NO URL PROVIDED")

def enumeration(): 
    
    print(Fore.BLUE + "Target Enumeration\n" + Style.RESET_ALL)
    os.system('gobuster dir -q -u' + results.url + '/ -w wordlist.txt -r -a "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36" --timeout 10s')

    while True: 
        enumeration_continue = input("Would you like to continue? ")
        if enumeration_continue == 'Yes' or enumeration_continue == 'yes':
                enumeration_new = input("Enter the directory name: ")
                os.system('gobuster dir -q -u' + results.url + '/' + enumeration_new + '/ -w wordlist.txt -r -a "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36" --timeout 10s')
                break
        else: 
            continue

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
    print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
    print(Fore.CYAN + ("❌ This tool is not intended for malicious purposes ❌") + Style.RESET_ALL)
    print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
    print(Fore.CYAN + ("❌ This tool is not intended for malicious purposes ❌") + Style.RESET_ALL)
    print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
    print("\n====================================================\n")
    cookie_check()
    print("\n====================================================\n")
    whois_ip()
    print("\n====================================================\n")
    input("Press enter to continue to enumeration")
    print("\n====================================================\n")
    enumeration()
    sys.exit()


