import os
from time import sleep
print('''

1 > Android

2 > Window

3 > Linux

''')
options = int(input('Chuse Your Operating System : '))
if options == 1:
    print('Please Wait While Creating The Environment For CEEP ....')
    os.system('rm -rf install.py')
    os.system('mkdir web')
    sleep(2)
    print('<<<--- Done.. ceep is installed now simpaly type python3 ceep.py .... --->>>')
    exit()
elif options == 2:
	print('')
	print('Sorry This Tools is not avaliable for windows Right now')
	exit()

elif options == 3:
    print('Please Wait While Creating The Environment For CEEP ....')
    os.system('rm -rf install.py')
    os.system('mkdir web')
    sleep(2)
    print('<<<--- Done.. ceep is installed now simpaly type python3 ceep.py .... --->>>')
    exit()
else:
    print('Chuse The Correct Options From Given Below ...')
    exit()