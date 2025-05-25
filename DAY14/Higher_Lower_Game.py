import random
# List of famous Instagram personalities with country and occupation
instagram_celebrities = [
    {"name": "Cristiano Ronaldo", "country": "Portugal", "occupation": "Footballer", "followers_millions": 652},
    {"name": "Lionel Messi", "country": "Argentina", "occupation": "Footballer", "followers_millions": 505},
    {"name": "Selena Gomez", "country": "USA", "occupation": "Singer, Actress", "followers_millions": 421},
    {"name": "Dwayne Johnson", "country": "USA", "occupation": "Actor, Wrestler", "followers_millions": 394},
    {"name": "Kylie Jenner", "country": "USA", "occupation": "Media Personality", "followers_millions": 394},
    {"name": "Ariana Grande", "country": "USA", "occupation": "Singer, Actress", "followers_millions": 376},
    {"name": "Kim Kardashian", "country": "USA", "occupation": "Media Personality", "followers_millions": 357},
    {"name": "Beyoncé", "country": "USA", "occupation": "Singer, Actress", "followers_millions": 312},
    {"name": "Khloé Kardashian", "country": "USA", "occupation": "Media Personality", "followers_millions": 303},
    {"name": "Justin Bieber", "country": "Canada", "occupation": "Singer", "followers_millions": 294},
    {"name": "Kendall Jenner", "country": "USA", "occupation": "Model, Media Personality", "followers_millions": 288},
    {"name": "Taylor Swift", "country": "USA", "occupation": "Singer", "followers_millions": 282},
    {"name": "Virat Kohli", "country": "India", "occupation": "Cricketer", "followers_millions": 271},
    {"name": "Jennifer Lopez", "country": "USA", "occupation": "Singer, Actress", "followers_millions": 249},
    {"name": "Neymar Jr.", "country": "Brazil", "occupation": "Footballer", "followers_millions": 229}
]
def Higher_Lower_Game(instagram_celebrities):
    game_over = False
    score = 0
    while game_over != True:
        choice1, choice2 = random.sample(instagram_celebrities, 2)
        print(f"{choice1["name"]} - {choice1["country"]} - {choice1["occupation"]}")
        print(f"{choice2["name"]} - {choice2["country"]} - {choice2["occupation"]}")
        user_choice = input("Who has more followers today? 'a' or 'b': ")
        user_choice = user_choice.lower()
        if user_choice == "a":
            if choice1["followers_millions"] > choice2["followers_millions"]:
                score += 1
                game_over = False
            else:
                game_over = True
                print("You lost")
        if user_choice == "b":
            if choice2["followers_millions"] > choice1["followers_millions"]:
                score += 1
                game_over = False
            else:
                game_over = True
                print("You lost")
        if choice1["followers_millions"] == choice2['followers_millions']:
            if user_choice == "a" or user_choice == "b":
                score += 1
                game_over = False
    print(f"Final Score is {score}")

Higher_Lower_Game(instagram_celebrities)
