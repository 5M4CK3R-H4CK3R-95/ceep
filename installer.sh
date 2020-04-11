#!/bin/bash
clear
echo "Please Wait While Seting up ceep for you ..."
apt install wget
clear
mkdir data
mkdir web
touch data/cp.txt
touch data/data.txt
touch data/os.txt
touch data/rc_name.txt
touch data/url.txt
mv ngrok data
chmod +x data/ngrok
rm -rf installer.sh
sleep 2
echo ""
echo "Done Ceep Is Sucessfully instaleld in your device now just simply type pytho3 ceep.py"
echo ""