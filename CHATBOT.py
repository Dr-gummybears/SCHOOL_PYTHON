import time

# asking for name
name = input("Please enter your name: ")
# asking for a location
town = input("Where do you live? ")

answer_raining = input("Hello " + name + ", is it raining in " + town + "? ")

# setting response to if its rainy or not
if answer_raining == "Yes":
    print("Oh dear, never mind!")
else:
    print("That's nice, have a good day.")

# sleep so next question isnt asked instantly
time.sleep(0.1)

age = int(input("How old are you? "))

time.sleep(0.1)

# asking if they are in school or not
if age <=  18:
    In_Education=input("Oh you are still at school? ")
    time.sleep(0.1)
    if In_Education == "Yes":
        School = input("What school do you go to then? ")
    else:
        print("You should be in school")
else:
    print("Oh you're not that old then! ")

# asking personal opinion on program (i got bored at this point)(this is designed to be the last one in the program)
oppinion = input("Do you like me? ")

if oppinion != "Yes":
    time.sleep(0.1)
    i = 1
    while i <= 200:
        print("Fuck YOU!")
        i = i+1
else:
    print("Oh that's good I like you to! Goodbye then.")
