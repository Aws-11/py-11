import sys


new_list = []


while True:
    inputname = (input("type here: "))
    if not inputname:
        print("no data entery!")
        
    
    elif len(new_list) >= 24:
        break
    
    else:
        new_list.append(inputname)
        print(len(new_list))
print(new_list)


sys.exit("you have reached the set limit of your list!")

