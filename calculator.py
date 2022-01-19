while (True):
    operation = str(input("Choose a. for addition b. for subtraction c. for multiplication d. for division\n"))
    n1 = float(input("Enter first number:- "))
    n2 = float(input("Enter second number:- "))
    if operation == "a":
        print("Result is:-", n1 + n2)
        continue
    elif operation == "b":
        print("Result is:-", n1 - n2)
        continue
    elif operation == "c":
        print("Result is:-", n1 * n2)
        continue
    elif operation == "d":
        print("Result is:-", n1 / n2)
        continue
    else:
        break