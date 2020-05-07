#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connHost(THost, TPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((THost,TPort))
		print '%d/tcp open' %TPort
	except:
		print '%d/tcp close' %TPort
	finally:
		sock.close()


def portScanner(THost,TPorts):
#If the user entered a host with domain name, so this exception loop finds the IP of the host to crack
	try:
		hostIP= gethostbyname(THost)
	except:
		print ' Unknown host ' + THost
#This loop is to state the scan is now being initiated so if the IP can be resolved by the command then it will display the domain name
#else it will display the ip of the host for the scan getting started
	try:
		hostName= gethostbyaddr(hostIP)
		print '[+]Scan results for ' + hostName
	except:
		print '[+]Scan results for ' + hostIP

	for TPort in TPorts:
		t= Thread(target = connHost , args = (THost,int(TPort)))
		t.start()



def main():
	parser = optparse.OptionParser('Usage syntax is' + '-H <targetHost> -p <targetPorts>')
	parser.add_option('-H', dest='THost', type= 'string', help = 'Enter the host you want to scan the ports on')
	parser.add_option('-p', dest='TPorts', type= 'string', help = 'Enter the ports separated by \',\'')
	(options ,args) = parser.parse_args()
	THost = options.THost
	TPorts = str(options.TPorts).split(',')
	if (THost == None) | (TPorts == None):
		print 'Unknown Error Occured'
		exit(0)
	portScanner(THost,TPorts)


if __name__ == '__main__':
	main()
