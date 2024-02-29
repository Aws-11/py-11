n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    element = input("Enter element {}: ". format(i+1))
my_list.append(element)

print("list  ", my_list)


