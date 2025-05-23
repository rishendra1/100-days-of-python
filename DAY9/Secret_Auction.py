Auction_details = {}
def Enter_Details():
    Name = input("What is your name? ")
    Amount = int(input("How much money would you like to bid? "))
    Auction_details[Name] = Amount
    option = input("Would you like to continue? - 'Y' or 'N' - ")
    if (option == "Y"):
        Enter_Details()
def Highest_Amount():
    bid_winner = max(Auction_details.values())
    for Name in Auction_details:
       if (bid_winner == Auction_details[Name]):
           return Name
print("Hello friends!! welcome to secret auction")
Enter_Details()
print(f"{Highest_Amount()} is the winner of this secret auction")

