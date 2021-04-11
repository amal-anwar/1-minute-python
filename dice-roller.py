import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dice")
    print("The values are")
    print(random.randint(min,max))
    roll_again = input("Roll the dice again? \n")
    print("\n")
    if roll_again == "yes":
        continue
