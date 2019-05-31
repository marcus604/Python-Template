#!/bin/sh
VENV_PYTHON=""                                  #pipenv --venv
PROJECT=""                                      #Project location
SCRIPT=".py"                                    #Script 
cd "${PROJECT}" && "${VENV_PYTHON}" "${SCRIPT}" #-a Arguments here


#       crontab -e
#       * * * * * ~/script.sh
#       | | | | |
#       | | | |  -> Weekday  (0=Sun .. 6=Sat)
#       | | |  ->>> Month    (1..12)
#       | |  ->>>>> Day      (1..31)
#       |  ->>>>>>> Hour     (0..23)
#        ->>>>>>>>> Minute   (0..59)