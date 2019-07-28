### play a sound through a buzzer connected to a pin
## HOW IT WORKS: 
## DEPENDENCIES:
# OS:
# Python: RPi.GPIO
## CONFIGURATION:
# required: pin, duration
# optional: 
## COMMUNICATION:
# INBOUND: 
# - NOTIFY: receive a notification request
# OUTBOUND: 

import RPi.GPIO

from buzzer import Buzzer

class Buzzer_raspi(Buzzer):
    gpio = RPi.GPIO