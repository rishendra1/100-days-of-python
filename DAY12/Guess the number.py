import random
List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,
        71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
def Guess_Number():
    Result = random.choice(List)
    choice1 = input("Difficulty level - Hard or Easy:")
    choice1 = choice1.lower()
    if choice1 == 'hard':
        chances = 5
        print(f"You have only {chances} chances")
    if choice1 == 'easy':
        chances = 10
        print(f"You have only {chances} chances")
    while chances > 0:
        n = int(input("Guess a number between 1 and 100: "))
        if n > 100 or n < 0:
            chances -= 1
            print(f"Sorry, that's not a number, {chances} chances are only left")
        if n < Result and n > 0:
            print("Too low")
            chances -= 1
            print(f"Sorry, that's not a number, {chances} chances are only left")
        if n > Result :
            print("Too high")
            chances -= 1
            print(f"Sorry, that's not a number, {chances} chances are only left")
        if n == Result:
            print("Congratulations !!!! it is Correct answer", Result)
            break
Guess_Number()