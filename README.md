# Hangman

<p align="center">
    <a href="https://coveralls.io/repos/github/jaywyawhare/Hangman">
        <img src="https://coveralls.io/repos/github/jaywyawhare/Hangman/badge.svg" alt="Coverage Status">
    </a>
</p>

This is a simple hangman game written in Python. It is a command line game. The game is a simple word guessing game. The game will generate a random word, and the player will have to guess the word. The player will have a 5 attempts to guess the word. The game will continue until the player guesses the word or runs out of attempts.

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/jaywyawhare/Hangman.git
    ```

2. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- Normal usage :
    1. Run the game

        ```bash
        python main.py
        ```

    2. The game will generate a random word and the player will have to guess the word.

- API usage :
    1. Run the API

        ```bash
        python api.py
        ```

    2. The API will be running on `http://localhost:5000/`. You can use the API to play the game or to get the word.

## API Endpoints

- `/word` [GET]: This endpoint will return a random word.
- `/hangman` [GET]: This endpoint will return the current state of the game. It will return the word, the current state of the word, the attempts left, and the status of the game.
- `/hangman` [POST]: This endpoint will take a letter as input and will return the updated state of the game.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [DBaJ-NC-CFL](./LICENCE.md).
