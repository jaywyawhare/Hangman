import random

def choose_word():
    with open ("src/words.txt", "r") as file:
        words = file.readlines()
        words = [word for word in words if word.strip()]
    return random.choice(words).strip()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_word_length(word):
    return len(word)