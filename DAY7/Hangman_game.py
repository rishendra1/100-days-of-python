# Hangman game
import random

words = [
    "sunset", "river", "mountain", "forest", "ocean",
    "galaxy", "comet", "thunder", "storm", "breeze",
    "flame", "shadow", "crystal", "echo", "whisper",
    "spark", "stone", "cloud", "mist", "blaze",
    "drift", "frost", "glide", "dust", "wave",
    "glow", "pulse", "ray", "wind", "leaf",
    "snow", "rain", "branch", "root", "sky",
    "nova", "orbit", "trail", "path", "light",
    "night", "dawn", "dusk", "flash", "surge",
    "chime", "glint", "quake", "star", "flare"
]

word = random.choice(words)
word_length = len(word)
result = ["_"] * word_length
life = word_length
print(word)
print(f"You have to guess a random word that consists of {word_length} letters")

while life > 0 and "_" in result:
    print("Word: ", " ".join(result))
    guess = input("Guess a random letter: ").lower()

    if guess in word:
        for i in range(word_length):
            if word[i] == guess:
                result[i] = guess
        print("Correct!\n")
    else:
        life -= 1
        print(f"Wrong guess. Lives left: {life}/{word_length}\n")

if "_" not in result:
    print("You win! The word was:", word)
else:
    print("You lost! The word was:", word)
