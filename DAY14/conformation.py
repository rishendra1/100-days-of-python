import random
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
choice1 = random.choice(instagram_celebrities)
print(choice1["name"] - choice1["followers_millions"])