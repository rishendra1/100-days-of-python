#Pizza Bill Calculator
Size = input("What is the size of the pizza? S,M or L - ")
pepperoni = input("Do you want to add extra pepperoni? Y or N - ")
cheese = input("Do you want to add extra cheese? Y or N - ")

if Size=="S":
    Bill = 15
    if pepperoni=="Y":
        Bill  = Bill + 1
if Size=="M":
    Bill = 20
    if pepperoni=="Y":
        Bill = Bill + 2
if Size=="L":
    Bill = 25
    if pepperoni=="Y":
        Bill = Bill + 3
if cheese=="Y":
    Bill = Bill + 1

print(f"Total Bill: {Bill}")

