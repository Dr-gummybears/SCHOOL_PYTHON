import time

Times = "*"
Minus = "-"
Add = "+"
Divide = "/"
# asking the operator
Operator = input("What operator do you want? + * / - **: ")
# defining the operator

if Operator == "*":  # If = *, multiply numbers
    First_No = int(input("What is the First number in your calculation: "))  # asking for first nummber in calculation
    Second_No = int(
        input("What is the Second number in your calculation: "))  # asking for Second nummber in calculation
    print("You answer is: ")
    time.sleep(0.2)
    print(First_No * Second_No)

elif Operator == "-":  # If = -, subtract numbers
    First_No = int(input("What is the First number in your calculation: "))  # asking for first nummber in calculation
    Second_No = int(
        input("What is the Second number in your calculation: "))  # asking for Second nummber in calculation
    print("You answer is: ")
    time.sleep(0.2)
    print(First_No - Second_No)

elif Operator == "+":  # If = +, add numbers
    First_No = int(input("What is the First number in your calculation: "))  # asking for first nummber in calculation
    Second_No = int(
        input("What is the Second number in your calculation: "))  # asking for Second nummber in calculation
    print("You answer is: ")
    time.sleep(0.2)
    print(First_No + Second_No)

elif Operator == "/":  # If = /, Divide numbers
    First_No = int(input("What is the First number in your calculation: "))  # asking for first nummber in calculation
    Second_No = int(
        input("What is the Second number in your calculation: "))  # asking for Second nummber in calculation
    print("You answer is: ")
    time.sleep(0.2)
    print(First_No / Second_No)

elif Operator == "**":  # If = **, Square numbers
    First_No = int(input("What is the First number in your calculation: "))  # asking for first nummber in calculation
    Second_No = int(
        input("What is the Second number in your calculation: "))  # asking for Second nummber in calculation
    print("You answer is: ")
    time.sleep(0.125)
    print(First_No ** Second_No)

time.sleep(0.125)
print("Thanks for your calculation. Bye!")


