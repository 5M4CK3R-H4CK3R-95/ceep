#!/usr/bin/python3
from time import sleep
from os import system
system('clear')
print('Please Wait While Setting up ceep for you ..')
sleep(2)
system('apt update')
system('clear')
system('mkdir data')
system('mkdir web')
system('touch data/cp.txt')
system('touch data/data.txt')
system('touch data/os.txt')
system('touch data/rc_name.txt')
system('touch data/url.txt')
system('unzip ngrok.zip')
system('clear')
system('mv ngrok data')
system('rm -rf ngrok.zip')
system('chmod +x data/ngrok')
system('chmod +x *')
system('rm -rf installer.py')
system('clear')
print('')
print('Done You Are Ready Now Just Type python3 ceep.py to start ceep .')
print('')
