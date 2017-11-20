




def start():
    characters = input("Enter characters and initiatives in the form character1/initiative1,character2/initiative2 ... etc : ").split(",")
    
    initiativeList = []


    for character in characters:
        initiativeList.append([character.split("/")[0], character.split("/")[1]])

    print(initiativeList)

    initiativeList.sort(key=lambda x: x[1])

    print(initiativeList)

    print(initiativeList[::-1])



start()