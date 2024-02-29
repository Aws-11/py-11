import sys





def br_game():
    class br(Enum):
        red = 1
        blue = 2
    playerchoice = door
    door = input("\nplease enter 1 for red  \n2 for blue ")
    if playerchoice not in ["1","2"]:
        return br_game()
        print("please enter 1 or 2")
    print("welcom to my game \nplease chose red or blue")
    

    player =int(playerchoice)
    print("\nyou chose " + str(br_game(player)). replace('br.','')+ ".")

    if player == 1 :
        box=input("\nplease enter 1 for red  \n2 for blue ")

    br_game()

    # door=input("ther is 2 doors 🚪Red and 🚪Blue \n").lower()
    # if door=="red":
    #     print("to 2th step")
    # if door!="red":
    #     print("lose")
    # box=input("choes one of thos Red📦Blue📦Yellow📦\n").lower()
    # if box =="red":
    #     print("get 💶💶")
    # else:
    #     print("try agin")