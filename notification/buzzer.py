# common functions for buzzer

from sdk.python.module.notification import Notification

import sdk.python.utils.exceptions as exception

class Buzzer(Notification):
    # What to do when initializing
    def on_init(self):
        self.config_schema = 1
        self.add_configuration_listener(self.fullname, "+", True)

    # What to do when running
    def on_start(self):
        # initialize GPIO
        self.gpio.setmode(self.gpio.BCM)
        self.gpio.setwarnings(False)
        self.gpio.setup(self.config["pin"], self.gpio.OUT)
        
    # What to do when shutting down
    def on_stop(self):
        pass
        
   # What to do when ask to notify
    def on_notify(self, severity, text):
        self.log_debug("activating buzzer on pin "+str(self.config["pin"])+" for "+str(self.config["duration"])+" seconds")
        self.gpio.output(self.config["pin"], self.gpio.HIGH)
        self.sleep(self.config["duration"])
        self.gpio.output(self.config["pin"], self.gpio.LOW)

     # What to do when receiving a new/updated configuration for this module    
    def on_configuration(self, message):
        # module's configuration
        if message.args == self.fullname and not message.is_null:
            if message.config_schema != self.config_schema: 
                return False
            if not self.is_valid_configuration(["pin", "duration"], message.get_data()): return False
            self.config = message.get_data()