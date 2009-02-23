#---------------------------------------------------------------------
#
#        Phantom Bot         Version : $VERSION$ 
#        By:
#                     lxsameer (Sameer Rahmani)
#                     lxsameer@lxsameer.org
#        Home page:          $HOMEPAGE$
#
#---------------------------------------------------------------------


import setting
import sys


def default_brain ():
    
    brain_module = __import__ ( setting.BRAIN , globals () , locals () , ["main"] , -1)
    
    obj = brain_module.main.Cbrain ()
    return obj 

default = default_brain ()
