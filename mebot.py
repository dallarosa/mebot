import sys
import socket
import string

HOST="172.16.171.150"
PORT=6667
NICK="Me"
IDENT="me"
REALNAME="I'm me"
readbuffer=""

def greeting(sock):
	sock.send("PRIVMSG #nlp hi!\r\n")

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

while 1:
	readbuffer=readbuffer+s.recv(1024)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop( )

	for line in temp:
		print line
		line=string.rstrip(line)
		line=string.split(line)

		if(line[0]=="PING"):
			s.send("PONG %s\r\n" % line[1])
		if(line[1]=="MODE"):
			s.send("JOIN #nlp\r\n")
		try:
			if "PRIVMSG" in line and (":Me" in line or ":Me," in line or ":Me:" in line):
				greeting(s)
		except ValueError:
			pass


