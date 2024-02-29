import random
print("welcome to my game")
print("choess one of thoes")
print("2 for random.randint")
print("1 for random.random")
choice=input("choice 1,2")
if choice == 1 :
   print(random.choice("123"))

else:

   print(random.choice("abc"))