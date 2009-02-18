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






def analyze (msg , nick , s):
    """analyze msg for a valide command"""
    
    if msg[0] == "!":
        command = msg[1:]
        # i must add dest channel
        # write proc needed
        if msg[1:] == "version\r\n":
            print "Recieved Version command."
            s.send ("PRIVMSG #alavnet : %s \r\n" % ( "Phantom bot version 0.1.0"))
        elif msg[1:] == "help\r\n":
            print "Recieved help command."
            s.send ("PRIVMSG #alavnet : %s \r\n" % ( "nothing ."))
        else:
           
            s.send ("PRIVMSG #alavnet : %s \r\n" % ( "I can't understand you . please refer to help section."))
    return 0



argnick = "Phantom_bot"
argident = ""
argowner = "Sameer Rahmani"

###    I should use optparser module here later
if sys.argv[1] != "":
    channellist = sys.argv[1].split (",")




HOST = 'irc.freenode.net'                                    #The server we want to connect to
PORT = 6667                                                  #The connection port which is usually 6667
NICK = argnick                                               #The bot's nickname
IDENT= argident
REALNAME = 'Phantom'
OWNER = argowner                                             #The bot owner's nick
CHANNELINIT = channellist                                    #The default channel for the bot
readbuffer = ''                                              #Here we store all the messages from server 



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


try:
        while 1:
            data = s.recv(1024)
            if data:
                print "data: " + unicode ( data)
                readbuffer = readbuffer + data
                temp = string.split ( readbuffer , "\n" )
                readbuffer = temp.pop( )
                
                if data.find ( 'PRIVMSG' ) != -1:
                    nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
                    message = ':'.join ( data.split ( ':' ) [ 2: ] )
                    print nick + ':', message
                    analyze ( message , nick , s)

except :
    pass

