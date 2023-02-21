from time import sleep
import gpiozero as gpio
import railgun
import airinjector
from utils import helpRegistry, railCommands, airinjectorCommands

railgunner = railgun.railgun()

injector = airinjector.airinjector()

def init():
   while True:
      variables = input('> ').split(" ")
      if variables[0] == "help" and len(variables) == 1:
         print("")
         for x in range(0, len(railCommands), 2):
            print("command " + railCommands[x] + " with " + str(railCommands[x + 1]) + " vars: ")
            print(helpRegistry[helpRegistry.index(railCommands[x]) + 1])
            print("")
      else:
         if variables[0] == "railgun":
            try:
               index = railCommands.index(variables[1])
               if index >= 0:
                  if len(variables) - 2 != railCommands[index + 1]:
                     print("wrong var #")
                     continue
                  else:
                     getattr(railgunner, variables[1])(variables)
            except ValueError:
               print("not a valid cmd")
         elif variables[0] == "injector":
            try:
               index = airinjectorCommands.index(variables[1])
               if index >= 0:
                  if len(variables) - 2 != index + 1:
                     print("wrong var #")
                     continue
                  else:
                     getattr(injector, variables[1])(*variables)
            except ValueError:
               print("not a valid cmd")
         else:
            print("identify command to *injector* or *railgun*")

init()