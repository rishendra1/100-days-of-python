import random
'''In this code I have used two integer variables a and b
Where a - denotes the user's choice and b is the computer's choice'''
a = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissor"))
b = random.randint(0,2)
if b == 0: print("I chose Rock")
if b == 1: print("I chose Paper")
if b == 2: print("I chose Scissor")

if a < 0 and a > 2:
    print("Invalid Choice")
elif a == 0 and b == 2 :
    print("You won. Rock wins")
elif a == 2 and b == 0 :
    print("Sorry!! You lost.Rock wins")
elif a == 1 and b == 2 :
    print("Sorry!! You lost. Scissor wins")
elif a == 2 and b == 1 :
    print("You won. Scissor wins")
elif a == 0 and b == 1 :
    print("Sorry!! You lost. Paper wins")
elif a == 1 and b == 0 :
    print("You won. Paper wins")
elif a==b:
    print("Its a tie")