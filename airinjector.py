from time import time, sleep
from gpiozero import OutputDevice

solenoid = OutputDevice(15)

OPTIMAL_FIRING_TIME = .0125

class airinjector:
    def __init__(self):
        self.init_time = time()
        
    def fire(self, seconds = OPTIMAL_FIRING_TIME):
        solenoid.on()
        sleep(seconds)
        solenoid.off()
    
    def test(self, seconds):
        self.fire(seconds)