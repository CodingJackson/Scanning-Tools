#!/usr/bin/python

from socket import *

def con(thost, tport):
	thost = gethostbyname(thost)
	s = socket(AF_INET,SOCK_STREAM)
	if s.connect((thost,tport)):
		print "Connection can't be established"
	else:
		s.send("hey its your boy \r\n")
		grab = s.recv(1024)
		print grab

con("lpu.in",443)
