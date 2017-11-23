#Imports
from colorama import init
init()
from colorama import Fore,Back,Style
import os
import time


#Initialize colorama
init()


#Set up global variables
combatants = []




#Takes a combatant name, and modifies the global combatants list to change that combatant into a tuple with itself and its initiative, from user input
def getInitiatives(combatant):
    global combatants

    initiative = input("What is the initiative of " + combatant + "?")
    combatants[combatants.index(combatant)] = [combatant,initiative]




#Enters the names of combatants into the global combatants list. Names are gotten from the user
def getCombatants():
    global combatants
    combatants = input("Enter names of combatants seperated by commas").split(",")




#Print out the initiative order. Combatant who's turn it is is highlighted
def printCurrentCombatants(i):
    for combatant in combatants:
        if (combatants.index(combatant) == i):
            print (Fore.RED + str(combatant) + Style.RESET_ALL)
        else:
            print(combatant)




#Takes a combatant name, and deletes the corresponding tuple from the global combatants list
def deleteCombatant(name):
    global combatants
    combatants = [i for i in combatants if i[0] != name]




#Contains the main combat loop, and loops through the initiative list, while handling user commands
def displayCombatStatistics():
    os.system('cls')

    i = 0

    while (True):

        #Loop back to the top of the initiative list
        if(i == len(combatants)):
            i = 0

        #Print out the initiative list
        printCurrentCombatants(i)
        
        #Slow it down to avoid multiple button presses per actual press
        #Then get user input
        time.sleep(0.250)
        x = input("Press enter to continue (q enter to quit, kill to kill a combatant)")


        #check commands -- blank command moves to next turn
        if (x == 'q'):
            os.system('cls')
            break

        if (x == 'kill'):
            y = input("Who died?")
            deleteCombatant(y)
        
        #if the user presses enter without any arguments, move to the next turn
        if (x == ''):
            os.system('cls')
            i = i + 1




#Sorts the global combatants list on the second element in each tuple
def sortCombatants():
    global combatants

    combatants.sort(key=lambda x: int(x[1]))
    combatants = combatants[:: -1]




#Makes initial function calls, and sets up for displayCombatStatistics
def start():
    getCombatants()

    for combatant in combatants:
        getInitiatives(combatant)

    sortCombatants()
    displayCombatStatistics()




#Prints the main screen, and starts up the program
def introduction():
    print("Hello world, welcome to the dynamic combat tracker")
    print("""
                   ___====-_  _-====___
           _--^^^#####//      \\\\#####^^^--_
        _-^##########// (    ) \\\\##########^-_
       -############//  |\^^/|  \\\\############-
     _/############//   (@::@)   \\\\############\_
    /#############((     \\\\//     ))#############\\
   -###############\\\\    (oo)    //###############-
  -#################\\\\  / VV \  //#################-
 -###################\\\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
    """)

    start()




#Calls the introduction to begin
introduction()