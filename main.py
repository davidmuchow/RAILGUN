from time import sleep
import gpiozero as gpio

thing = gpio.DigitalOutputDevice(17)

def init():
   while True:
      print('iteration')
      variable = input('input something!: ')
      if variable.find("fire"):
         thing.on()
         sleep(.25)
         thing.off()
      else:
         print("non")
         
init()