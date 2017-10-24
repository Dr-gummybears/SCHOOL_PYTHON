import time

opinion = input("Do you like me? ")

if opinion == "Yes":
    print("Oh that's good I like you to! Goodbye then.")
else:
    time.sleep(0.1)
    i = 1
    while i <= 200:
        print("Fuck YOU!")
        i = i+1
