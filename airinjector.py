from time import time, sleep
from gpiozero import OutputDevice

solenoid = OutputDevice(17)

OPTIMAL_FIRING_TIME = .0125

class airinjector:
    def __init__(self):
        self.init_time = time()
        
    def fire(self, seconds = OPTIMAL_FIRING_TIME):
        print("on!")
        solenoid.toggle()
        sleep(seconds)
        print("off!")
        solenoid.toggle()
        
    
    def test(self, *args):
        self.fire(float(args[2]))