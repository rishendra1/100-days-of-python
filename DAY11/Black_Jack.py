import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def check_winner(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 21 and len(user_hand) == 2:
        return "Blackjack! You win!"
    elif computer_score == 21 and len(computer_hand) == 2:
        return "Computer got Blackjack. You lose!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"

def play_blackjack():
    global user_hand, computer_hand
    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_hand.append(draw_card())
        computer_hand.append(draw_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"\nYour cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ")
            if choice == 'y':
                user_hand.append(draw_card())
            else:
                game_over = True

    while calculate_score(computer_hand) < 17:
        computer_hand.append(draw_card())

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"\nYour final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(check_winner(user_score, computer_score))

if input("Do you want to play Blackjack? (y/n): ").lower() == 'y':
    play_blackjack()
else:
    print("Thanks for stopping by!")
