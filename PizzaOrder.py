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
pizzas = {}
class Pizza:
   def __init__(self, number):
      def _getMenuCode():
         while (True):
            menuCode = input("Please enter a 3 letter/number menu code for pizza number " + str(number+1) +".\n>")
            #SC2 Validity checks
            #Check if menu code is in range
            if (len(menuCode) == 3):
               #Check for symbols
               #Validity variable
               canContinue = True
               for letter in menuCode:
                  if (letter.isdigit() or letter.isalpha()):
                     pass
                  else:
                     #print("BOO!!!", letter)
                     canContinue = False
               if (canContinue == True):
                  #Save data
                  self.menuCode = menuCode
                  break
               else:
                  print("\nCombination must only contain letters or numbers!\n\n")
                  continue
            else:
               print("\nCombination must have 3 letters or numbers!\n\n")
               continue
      def _getMenuName():
         #SC3 get the name of the menu item
         menuName = input("Please enter the menu name for " + self.menuCode + ".\n>")
         
      def _getInventoryQuantity():
         print(str(number))
      _getMenuCode()
      _getMenuName()
      _getInventoryQuantity()
#SC1 Prompt the user to input the number of simulated pizzas they would like
#Set up exception check loop
while (True):
   numberOfPizzas = input("Hello! How many simulated pizzas would you like to create? (Must be between 1 and 10)\n>")
   #SC1 Check the validity of the user input
   #Check if is int
   if (numberOfPizzas.isnumeric()):
      #Input is a number!
      numberOfPizzas = int(numberOfPizzas)
      #Check if is in range
      if (numberOfPizzas >= 1 and numberOfPizzas <= 10):
         print("\nYou entered: " + str(numberOfPizzas) + "\n")
         break
      else:
         print("\nPlease enter a number between 1 and 10!\n\n")
         continue
   else:
      print("\nPlease enter a number!\n\n")
      continue

#SC2 Get menu codes, names, and quanities of the pizzas
#Create an interation variable
i = 0
while (i < numberOfPizzas):
   #pizzas[i]
   #Menu code for item i
   pizzas[i] = Pizza(i)
   #Increment the variable to target next item on the next iteration
   i+=1
