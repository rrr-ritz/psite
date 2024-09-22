print("___________________________\n" + 
      "| Console Calculator v2.0 |\n" + 
      "---------------------------\n")

choice = "y"
calcNum = 1

while(choice == "y"):
    print(f"\n Calculation {calcNum}\n" + 
             "----------------")
    
    num1 =     float(input("First Number ===>\t"))
    operator =       input("Operator =======>\t")
    num2 =     float(input("Second Number ==>\t"))

    calcNum += 1

    if operator == "+":
        print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 + num2}")
    elif operator == "-":
        print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 - num2}")
    elif operator == "*":
        print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 * num2}")
    elif operator == "/":
        if num2 == 0:
            calcNum -= 1
            print("\n** Can't divide by zero. Try again... **\n")
            continue
        else:
            print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 / num2}")
    elif operator == "**":
        print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 ** num2}")
    elif operator == "%":
        print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 % num2}")
    else:
        calcNum -= 1
        print("\n** That's an invalid operator. Try again... **\n")
        continue

    choice = input("\n\nWould you like to perform another calculation? (y/n) ==>\t")
    choice = choice.lower()

    if choice == "n":
        print("__________________________\n" + 
              "| OK, happy calculating! |\n" + 
              "--------------------------")