




combatants = []




def getInitiatives(combatant):
    initiative = input("What is the initiative of " + combatant + "?")
    combatants[combatant] = [combatant,initiative]




def getCombatants():
    combatants = input("Enter names of combatants seperated by commas").split(",")




def start():
    getCombatants()
    for combatant in combatants:
        getInitiatives(combatant)




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