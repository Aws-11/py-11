
def cr_calculator():
    calc = input("Type calculation:\n")
    print("Answer: " + str(eval(calc)))    
    last_calculation =[]
    if last_calculation == False:
        print("no last calculation")
    else:
        last_calculation.append(eval(calc))
        print(f"your last calculation is:  {last_calculation[-1]}")

    print("\n calculate again ?")
    while True:
        calculate_again = input("\nY for using the calculator again\nN for No\n.")
        if calculate_again.lower() not in ["y", "n"]:
            continue
        
        else:
            break

    if calculate_again.lower() == "y":
        return cr_calculator()
    else:
        print("thank you for using my calculator")

cr_calculator()


# def history():
#     global last_calculation

#     while True:
        
    
