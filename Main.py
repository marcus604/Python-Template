#Custom
from Classes import *
from config import *
from log import getLogger

#Libraries
from log import logging

import sys

##########CHANGE ME#################
PROGRAM_NAME = "NAME HERE"

logger = getLogger(__name__, "logs/{}.log".format(PROGRAM_NAME))

MODE_READ_ONLY = False
MODE_VERBOSE = False


def logLaunch():
    logger.info("Starting {}".center(40, "=").format(PROGRAM_NAME))
    


##################################################
#################Main Application#################
##################################################
def main():
    #Log startup
    logLaunch()

    
    logger.info("Finished {}".center(40, "=").format(PROGRAM_NAME))

    
        
    
    
##################################################
#####################Launcher#####################
##################################################
if __name__ == "__main__":

    VERBOSE_FLAG = "-v"         
    READ_ONLY_FLAG = "-r"       
    

    logLevel = logging.INFO
    if len(sys.argv) != 1:
        for arg in sys.argv[1:]:
            if arg == VERBOSE_FLAG:
                logLevel = logging.DEBUG
                MODE_VERBOSE = True
            if arg == READ_ONLY_FLAG:
                MODE_READ_ONLY = True
    
    logger.setLevel(logLevel)
    main()
