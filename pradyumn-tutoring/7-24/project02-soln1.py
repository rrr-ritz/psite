print("___________________________\n" 
      "| Console Calculator v1.0 |\n" 
      "---------------------------\n")

num1 = float(input("First Number ===>\t"))
operator =   input("Operator =======>\t")
num2 = float(input("Second Number ==>\t"))

if operator == "+":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 + num2}")
elif operator == "-":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 - num2}")
elif operator == "*":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 * num2}")
elif operator == "/":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 / num2}")
elif operator == "**":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 ** num2}")
elif operator == "%":
    print(f"CALCULATION:\t{num1} {operator} {num2} = {num1 % num2}")
