#Created By: Milad Khoshdel
#Special Thanks: Mikili
#Blog: https://blog.regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkho5hdel

import socket
import subprocess
import ipaddress
import urllib2

def banner():
	print(' ')
	print(' ################################################################################################')
	print(' ##                                                                                            ##')
	print(' ##                         __  __ ___ _      _   __  __ ___ _  __                             ##')
	print(' ##                        |  \/  |_ _| |    /_\ |  \/  |_ _| |/ /                             ##')
	print(" ##                        | |\/| || || |__ / _ \| |\/| || || ' <                              ##")
	print(' ##                        |_|  |_|___|____/_/ \_\_|  |_|___|_|\_\                             ##')
	print(' ##                                                                                            ##')
	print(' ##                                                             BY: Milad Khoshdel | Mikili    ##')
	print(' ##                                                             Blog: https://blog.regux.com   ##')
	print(' ##                                                                                            ##')
	print(' ################################################################################################')
	print(' ') 

banner()

range_host = raw_input('Enter IP Range (Example: 192.168.0.0/24) > ')

net1 = unicode(range_host)
net2 = ipaddress.ip_network(net1)

pma_401 = []
pma_200 = []

for x in net2.hosts():
    try:
        connection = urllib2.urlopen("http://" + str(x) + "/phpmyadmin", timeout=2)
        print str(x) + "\t" + str(connection.getcode())
        if connection.getcode() == 200:
		    pma_200.append(str(x))
        connection.close()
    except urllib2.HTTPError, e:
        print str(x) + "\t" + str(e.getcode())
        if e.getcode() == 401:
		    pma_401.append(str(x))
    except urllib2.URLError, e:
        print str(x) + "\tDown"
    except:
        print str(x) + "\tTimeout"

print "\n-----------------------------"
print "  URL Found With Credential  "
print "-----------------------------"
		
for y in pma_401: 
    print "[-] http://" + y + "/phpmyadmin"

print "\n--------------------------------"
print "  URL Found Without Credential  "
print "--------------------------------"

for z in pma_200: 
    print "[-] http://" + z + "/phpmyadmin"
