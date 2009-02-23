#---------------------------------------------------------------------
#
#        Phantom Bot         Version : $VERSION$ 
#        By:
#                     lxsameer (Sameer Rahmani)
#                     lxsameer@lxsameer.org
#        Home page:          $HOMEPAGE$
#
#---------------------------------------------------------------------


import os , sys
import setting

#-----------------------------
# don't modify this part
PHANTOM_VERSION=None
XBRAIN_VERSION=None
#-------------------------------



VERSION = PHANTOM_VERSION or  "0.2.0"
XVERSION = XBRAIN_VERSION or "0.1.0"





def version ():
    return "Phantom bot version " + VERSION + " using X-Brain version " + XVERSION

def help ():
    return "nothing yet"
    #txt = "Command list :\t"
    #for i in commandlist:
    #    hlp = i[2] or "N/A"
    #    txt = txt + "\t" + i[0] + "\t" + hlp + "\t"
    #return txt



# add your command and it action here

commandlist = [
    ("help" , help  , "Show this note") ,
    ("version" , version   , "Show bot version"),

]








class Cbrain :
    
    def __init__ (self):
        
        pass
    

    def analyze (self , nick , msg , cmd , target , data = None):
        
        if cmd ==  'PRIVMSG' :
            if msg[0] == "!" :
                command = msg[1:]
                print "Command : " + command
                argv = command.split (" ")
                arg = []
                for i in argv:
                    arg.append (i.replace ("\r\n" , ""))
                    print i
                cmd_name = arg[0]
                args = arg[1:]
                print "cmd_name : " + cmd_name + "   args : " + str(arg)
                return self.command_analyzer ( cmd_name , args )



    def command_analyzer (self , cmd , arg ):
        
        for i in commandlist:
            if cmd == i[0] :
                
                func = i[1]
                
                return func ()
        print "Command not found !."
        return "Command not found . Try !help for list of commands."


        
