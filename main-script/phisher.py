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
urlscan_api = os.environ.get('URLSCAN_API_KEY')
netcraft_api = os.environ.get('PHISHING_API_EMAIL')
custom_fig = Figlet(font='graffiti')
author =  Figlet(font='graceful')
version = "Version: V1"

# urlscan.io API details. This is to get the JSON results from a website scan 

def urlscan(): 
    
    headers = {'API-Key':urlscan_api,'Content-Type':'application/json'}
    data = {"url": phishing_url, "visibility": "unlisted"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    response_json = response.json()['uuid']
    print("\nCheck a screenshot for malicious content at this link: https://urlscan.io/screenshots/" + str(response_json) + ".png")
def netcraft_post():
    r = requests.post('https://report.netcraft.com/api/v3/test/report/urls', json={
    "email": netcraft_api,
    "urls": [{ "url": phishing_url, "country": "GB" }],
        })
    print(Fore.BLUE + "Netcraft" + Style.RESET_ALL)
    print( "\n Reported to Netcraft as an malicious url with ID: " + r.json()['uuid'])
    
def enumeration(): 
    print(Fore.BLUE + "Target Enumeration" + Style.RESET_ALL)
    os.system('gobuster dir -q -u' + phishing_url + '/ -w dicc.txt -r')

def whois_ip():
    domain = whois.query(phishing_url)
    domainip = socket.gethostbyname(phishing_url)
    c = Client()
    r = c.lookup(domainip)
    print(Fore.BLUE + "Site Information" + Style.RESET_ALL)
    print("\nDomain name: " + domain.name)
    print("Creation date: " + str(domain.creation_date))
    print("Registrant: " + domain.registrant)
    print("IP Address: " + domainip)
    print("ASN: " + r.asn)
    print("ASN Owner: " + r.owner)
 

while True: 

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + custom_fig.renderText("ConPhisher") + Style.RESET_ALL)
    print(Fore.CYAN + ("👉 github.com/raid-sailor") + Style.RESET_ALL)
    urlscan()
    menu_input = input("\nWould you like to continue to (yes/no): ") 

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



