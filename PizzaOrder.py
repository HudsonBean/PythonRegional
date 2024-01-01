import random
import math

class Pizzas:   
   
   def __init__(self, menuCode, menuName, quantity):
            print("Hello World!")
   def getValue(self): 
      print("")
   
   def toString(self):
      print("H")

########################
########################
#DRIVER SECTION
      #Enter your code below
#Variables
      
#SC1 Prompt the user to input the number of simulated pizzas they would like
numberOfPizzas = input("Hello! How many simulated pizzas would you like to create? (Must be between 1 and 10)\n>")
#Set up exception check loop
while (True):
   #SC1 Check the validity of the user input
   #Check if is int
   if (numberOfPizzas.isnumeric()):
      #Input is a number!
      numberOfPizzas = int(numberOfPizzas)
      #Check if is in range
      if (numberOfPizzas >= 1 and numberOfPizzas <= 10):
         print("\nYou entered: " + str(numberOfPizzas))
         break
      else:
         print("\nPlease enter a number between 1 and 10!\n\n")
         continue
   else:
      print("\nPlease enter a number!\n\n")
      continue

#SC2 Get some menu codes for the pizzas they want generated
for i in 3:
   print(i)
   