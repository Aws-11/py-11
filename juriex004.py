def smallest(list):
    small= min(list)
    return small



def min_input():
    x =int(input("input your x : "))
    y =int(input("input your y: "))
    
    if x < y:
        li=[]
        for i in range(1,x):
            li.append(i)
        print(i, end=" ")
        print("smallest in ",li,"is")
        print(smallest(li))
            

        
            

        

    elif x == y:
        print("x is equall to y")
    else:
        li=[]
        for i in range(1,y):
            li.append(i)
        print(i, end=" ")
        print("smallest in ",li,"is")
        print(smallest(li))

    

min_input()

