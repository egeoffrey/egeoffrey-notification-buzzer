### play a sound through a buzzer connected to a pin
## HOW IT WORKS: 
## DEPENDENCIES:
# OS:
# Python: OPi.GPIO
## CONFIGURATION:
# required: pin, duration
# optional: 
## COMMUNICATION:
# INBOUND: 
# - NOTIFY: receive a notification request
# OUTBOUND: 

import OPi.GPIO

from buzzer import Buzzer

class Buzzer_orangepi(Buzzer):
    gpio = OPi.GPIO