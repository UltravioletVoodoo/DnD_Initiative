from colorama import init
init()
from colorama import Fore,Back,Style
import os
import time



combatants = []




def getInitiatives(combatant):
    global combatants

    initiative = input("What is the initiative of " + combatant + "?")
    combatants[combatants.index(combatant)] = [combatant,initiative]




def getCombatants():
    global combatants
    combatants = input("Enter names of combatants seperated by commas").split(",")




def displayCombatStatistics():

    os.system('cls')

    i = 0

    while (True):

        if(i == len(combatants)):
            i = 0

        for combatant in combatants:
            if (combatants.index(combatant) == i):
                print (Fore.GREEN + str(combatant))
                print(Style.RESET_ALL)
            else:
                print(combatant)
        
        time.sleep(0.250)
        x = input("Press enter to continue (q enter to quit)")

        os.system('cls')
        i = i + 1

        if (x == 'q'):
            break




def sortCombatants():
    global combatants

    combatants.sort(key=lambda x: int(x[1]))
    combatants = combatants[:: -1]




def start():
    getCombatants()

    for combatant in combatants:
        getInitiatives(combatant)

    sortCombatants()

    displayCombatStatistics()




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




introduction()