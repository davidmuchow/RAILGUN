from time import time, sleep
from gpiozero import OutputDevice

# solenoid = OutputDevice(17)

OPTIMAL_FIRING_TIME = .0125

class airinjector:
    def __init__(self):
        self.init_time = time()
        
    def fire(self, seconds = OPTIMAL_FIRING_TIME):
        print("on!")
        sleep(seconds)
        print("off!")
    
    def test(self, *args):
        self.fire(float(args[2]))