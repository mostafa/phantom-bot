#! /usr/bin/env python

#---------------------------------------------------------------------
#
#        Phantom Bot         Version : $VERSION$ 
#        By:
#                     lxsameer (Sameer Rahmani)
#                     lxsameer@lxsameer.org
#        Home page:          $HOMEPAGE$
#
#---------------------------------------------------------------------



import os
import sys
import socket
import string
import time
import brains



def _assert (s):
    if DEBUG == 1 :
        print s



def irc_write (msg , target ,  s):
    s.send ("PRIVMSG %s : %s \r\n" % (target , msg))


argnick = "Phantom_bot"
argident = ""
argowner = "Sameer Rahmani"

###    I should use optparser module here later
if sys.argv[1] != "":
    channellist = sys.argv[1].split (",")


DEBUG = 1

HOST = 'irc.freenode.net'                                    #The server we want to connect to
PORT = 6667                                                  #The connection port which is usually 6667
NICK = argnick                                               #The bot's nickname
IDENT= argident
REALNAME = 'Phantom'
OWNER = argowner                                             #The bot owner's nick
CHANNELINIT = channellist                                    #The default channel for the bot
readbuffer = ''                                              #Here we store all the messages from server 

brain = brains.default





## making connection


s = socket.socket( )                                         #Create the socket
try:
    print "Connecting to irc.freenode.net . . . "
    s.connect(( HOST , PORT ))                                   #Connect to server
except:
    print "connecting faild !"
    sys.exit (1)
time.sleep ( 0.2 )
print "Trying to get nickname . . ."
s.send( "NICK %s\r\n" % NICK )
time.sleep( 0.2 )
print "Trying to set information . . ."
s.send( "USER %s  %s Phantom :%s\r\n" % ( NICK, HOST, REALNAME ))
print s.recv( 4096 )
time.sleep( 0.2 )
for i in channellist:
    s.send( "JOIN %s\r\n" % i)
    print s.recv(4096)
    print "Entering %s . . ."  % i



while 1:
    data = s.recv(1024)
    if data:
        
        #_assert ( "data: " + unicode ( data))
        readbuffer = readbuffer + data

        nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
        message = ':'.join ( data.split ( ':' ) [ 2: ] )
        command = data.split (" ") [1]
        target = data.split (" ") [2]
        #_assert ("assert : " + command + " " + target )
        print nick + ':', message
        a = brain.analyze (nick , message , command , target , data)
        if a:
            irc_write (a , target , s)

                

#except :
#    print "Connection Error !"
#    sys.exit (1)

