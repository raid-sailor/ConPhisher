#!/bin/bash

clear 
echo "1️⃣  Run the following command in a new terminal: touch ~/.bash_profile"
echo
echo "Press enter once you've completed this 👉 "
read 
clear
echo "2️⃣  Use the following command in a new terminal: nano  ~/.bash_profile"
echo
echo "Press enter once you've completed this 👉 "
read
clear
echo "3️⃣  Enter the following line in ~/.bash_profile: export PHISHING_API_EMAIL=""YOUR EMAIL"""
echo
echo "Press enter once you've completed this 👉 "
read 
clear
echo "4️⃣  Enter the following line on a new line in ~/.bash_profile: export URLSCAN_API_KEY=""YOUR API KEY"""
echo
echo "Press enter once you've completed this 👉 "
read 
clear
echo "5️⃣  Run the following command to make sure the variables appear in a new terminal session: env "
echo
echo "Press enter once you've completed this 👉 "
read 
clear 
echo "Setting up packages 🙌 "
echo
pip install -r main-script/requirements.txt
clear
echo "🎉 All done! Just head over to the main-script folder and run the following command: python3 phisher.py YOUR-TARGET-SITE 🎉"