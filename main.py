'''
GUN = 0
SNAKE = 1
WATER = -1

'''

import random

computer = random.choice([1, -1, 0])
youStr = input("Enter your Choice : ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youStr]


print(f"You choose {reverseDict[you]}\n Computer Chose {reverseDict[computer]}")


if(computer == you):
    print("It's a Draw")

else:
    if(computer == 0 and you == 1):       # snake cannot do anything to gun so you loose   
        print("You Loose")

    elif(computer == 0 and you == -1):    # water can take gun so you win
        print("You WIN")

    elif(computer == 1 and you == 0):     # Gun can Shot  snake so you win
        print("YOu WIN")

    elif(computer == 1 and you == -1):    # water cannot flow with snake so you loose
        print("You Loose")

    elif(computer == -1 and you == 0):    # Gun cannot shot in water so you loose 
        print("You Loose")

    elif(computer == -1 and you == 1):    # Sanke can swim in water so you win
        print("You WIN")

    else:
        print("Invalid Output")