#Libraries
from configparser import ConfigParser
import sys

#Custom
from Classes import *
from log import getLogger, logging

##########CHANGE ME#################
PROGRAM_NAME = "NAME HERE"

logger = getLogger(__name__, "logs/{}.log".format(PROGRAM_NAME))

MODE_READ_ONLY = False
MODE_VERBOSE = False


def logLaunch():
    logger.info("Starting {}".center(40, "=").format(PROGRAM_NAME))
    if MODE_READ_ONLY:
        logger.info("Read Only Mode".center(40, "="))
    if MODE_VERBOSE:
        logger.info("Verbose Logging".center(40, "="))

    


##################################################
#################Main Application#################
##################################################
def main():
    #Log startup
    logLaunch()

    #Get config file
    config = ConfigParser()

    config.read("config.ini")
    userConfig = config["USER_PREFERENCES"]

    API_KEY = userConfig["API_KEY"]
    
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
