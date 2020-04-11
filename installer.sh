#!/usr/bin/env bash
clear
echo "Please Wait While Seting up ceep for you ..."
sleep 2
apt install wget
clear
mkdir data
mkdir web
touch data/cp.txt
touch data/data.txt
touch data/os.txt
touch data/rc_name.txt
touch data/url.txt
unzip ngrok.zip
mv ngrok data
rm -rf ngrok.zip
chmod +x data/ngrok
chmod +x *
rm -rf installer.sh
echo ""
echo "Done Ceep Is Sucessfully instaleld in your device now just simply type pytho3 ceep.py"
echo ""
