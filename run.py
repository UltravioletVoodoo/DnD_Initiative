




combatants = []




def getInitiatives(combatant):
    global combatants

    initiative = input("What is the initiative of " + combatant + "?")
    combatants[combatants.index(combatant)] = [combatant,initiative]




def getCombatants():
    global combatants
    combatants = input("Enter names of combatants seperated by commas").split(",")




def displayCombatStatistics():
    for combatant in combatants:
        print(combatant)



def start():
    getCombatants()

    for combatant in combatants:
        getInitiatives(combatant)

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