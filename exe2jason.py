import json



from ex3json import createData, check_data

createData()
check_data

print("")
get_inp= input("DO YOU WISH TO DELETE YOUR DATA: Y FOR YES/ N FOR NO ")  
if get_inp.lower() in ("yes", "y"):
    with open('data2.json', 'w') as f:
        f.write("")
        print("DATA HAS BEEN DELETED")
else:
    print("confirmation failed")
    print("exiting")
exit()







