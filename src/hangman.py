from src.file_operations import choose_word, display_word, get_word_length

def draw_hangman(attempts):
    hangman_art = [
        "  ------\n      |\n       |\n       |\n       |\n       |\n",
        "  ------\n  |    |\n       |\n       |\n       |\n       |\n",
        "  ------\n  |    |\n  O    |\n       |\n       |\n       |\n",
        "  ------\n  |    |\n  O    |\n  |    |\n       |\n       |\n",
        "  ------\n  |    |\n  O    |\n /|\\   |\n       |\n       |\n",
        "  ------\n  |    |\n  O    |\n /|\\   |\n / \\   |\n       |\n"
    ]

    if attempts < len(hangman_art):
        print(hangman_art[attempts])
    else:
        print("Hangman art not available for this attempt.")

def hangman():
    word_to_guess = list(choose_word())
    guessed_letters = set()
    attempts = 5
    current_position = 0 

    print("Welcome to Hangman!")
    print("Length of the word to guess: " + str(get_word_length(word_to_guess)))

    while attempts > 0 and current_position < len(word_to_guess):
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent word: " + " ".join(current_display))
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts}")

        guess = input("Enter the next letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess != word_to_guess[current_position]:
            attempts -= 1
            print("Incorrect guess!")
            draw_hangman(5 - attempts)
        else:
            guessed_letters.add(guess)
            current_position += 1

    if current_position == len(word_to_guess):
        print("Congratulations! You guessed the word: " + "".join(word_to_guess))
    else:
        print("Sorry, you ran out of attempts. The word was: " + "".join(word_to_guess))
        print("Man hanged!")
        exit(0)

