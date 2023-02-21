from time import time, sleep
from tqdm import tqdm
import airinjector
import keyboard

class railgun:
    def __init__(self):
        self.init_time = time()
        self.airinjector = airinjector.airinjector()
        self.warm = False
        self.currentI = 0
        
    def warmup(self, *variables):
        print("starting 7 minute warmup... hold F to cancel")
        for i in tqdm (range(self.currentI, int(300 / (.0125))), desc="Loading"):
            if keyboard.is_pressed("f"):
                self.currentI = i
                break
            sleep(.0125)
        self.warm = True
            
    def activate(self, *variables):
        print(variables)
        