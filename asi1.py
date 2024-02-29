list = []

while True :
    list.append(input("enter index: "))
    if len(list)>= 5:
        for x in list:
            print(x)
        print ("\n","exiting"), exit()