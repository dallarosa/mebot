import sys
import socket
import string

HOST = sys.argv[1]
PORT = 6667
NICK = "DallaRosa_"
IDENT = "me"
REALNAME = "I'm me"
readbuffer = ""

class Response:
  RPL_WELCOME = "001"
  RPL_YOURHOST = "002"
  RPL_MYINFO = "004"
  RPL_BOUNCE = "005"
  RPL_USERHOST = "302"
  RPL_ISON = "303"
  RPL_AWAY = "301"
  RPL_UNAWAY = "305"
  RPL_NOWAWAY = "306"
  RPL_WHOISUSER = "311"
  RPL_WHOISSERVER = "313"
  RPL_WHOISIDLE = "317"
  RPL_ENDOFWHOIS = "318"
  RPL_WHOISCHANNELS = "319"
  RPL_WHOWASUSER = "314"
  RPL_ENDOFWHOWAS = "369"
  RPL_LIST = "322"
  RPL_LISTEND = "323"
  RPL_UNIQOPIS = "325"
  RPL_CHANNELMODEIS = "324"
  RPL_NOTOPIC = "331"
  RPL=TOPIC = "332"
  RPL_INVITING = "341"
  RPL_SUMMONING = "342"
  RPL_INVITELIST = "346"
  RPL_ENDOFINVITELIST = "347"
  RPL_EXCEPTLIST = "348"
  RPL_ENDOFEXCEPTLIST = "349"
  RPL_VERSION = "351"
  RPL_WHOREPLY = "352"
  RPL_ENDOFWHO = "315"
  RPL_NAMREPLY = "353"
  RPL_ENDOFNAMES = "366"
  RPL_ENDOFNAMES = "364"
  RPL_ENDOFLINKS = "365"
  RPL_BANLIST = "367"
  RPL_ENDOFBANLIST = "368"
  RPL_INFO = "371"
  RPL_ENDOFINFO = "374"
  RPL_MOTDSTART = "375"
  RPL_MOTD = "372"
  RPL_ENDOFMOTD = "376"
  RPL_YOUREOPER = "381"
  RPL_REHASHING = "382"
  RPL_YOURESERVICE = "383"
  RPL_TIME = "391"
  RPL_USERSSTART = "392"
  RPL_USERS = "393"
  RPL_ENDOFUSERS = "394"
  RPL_NOUSERS = "395"


def greeting(sock):
  sock.send("PRIVMSG #nlp hi!\r\n")

s = socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

while 1:
  readbuffer = readbuffer+s.recv(1024)
  temp = string.split(readbuffer, "\n")
  readbuffer = temp.pop( )

  for line in temp:
#    print line
    line = string.rstrip(line)
    line = string.split(line)
    if(line[0] == "PING"):
      s.send("PONG %s\r\n" % line[1])
    if(line[1] == Response.RPL_WELCOME):
      print "LOGGED IN"
      s.send("JOIN #nlp\r\n")
    try:
      if "PRIVMSG" in line and (":Me" in line or ":Me," in line or ":Me:" in line):
        greeting(s)
    except ValueError:
      pass
