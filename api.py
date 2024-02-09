from flask import Flask, request, jsonify
from src.file_operations import choose_word, display_word
from typing import Set

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "Endpoints": {
            "/hangman [Get]": "Print the current state of the word to guess along with the attempts left",
            "/hangman [Post]": "Make a guess",
            "/word [Get]": "Get the word to guess"
        },

        "Input format for POST request": {
            "guess" : "The letter you want to guess"
        }
    })


@app.route('/hangman', methods=['GET'])
def hangman_get():
    global guessed_letters, attempts, word_to_guess

    current_display = display_word(word_to_guess, guessed_letters)
    return jsonify({
        "Current word": " ".join(current_display),
        "Guessed letters": sorted(guessed_letters),
        "Attempts left": attempts
    })

@app.route('/hangman', methods=['POST'])
def hangman_post():
    global guessed_letters, attempts, word_to_guess

    if attempts == 0:
        return jsonify({
            "Message": "Sorry, you ran out of attempts. The word was: " + "".join(word_to_guess),
            "Status": "Game Over"
        })

    guess = request.json.get('guess', '').lower()

    if len(guess) != 1 or not guess.isalpha():
        return jsonify({
            "Message": "Please enter a single letter.",
            "Status": "Invalid Input"
        })

    if guess in guessed_letters:
        return jsonify({
            "Message": "You've already guessed that letter. Try again.",
            "Status": "Invalid Input"
        })

    if guess not in word_to_guess:
        attempts -= 1
        return jsonify({
            "Message": "Incorrect guess!",
            "Status": "Incorrect"
        })

    guessed_letters.add(guess)
    return jsonify({
        "Message": "Correct guess!",
        "Status": "Correct"
    })

@app.route('/word', methods=['GET'])
def word():
    global word_to_guess
    return jsonify({
        "Word to guess": "".join(word_to_guess)
    })

guessed_letters: Set[str] = set()
if __name__ == '__main__':
    word_to_guess = list(choose_word())
    attempts = 5
    app.run(debug=True)
