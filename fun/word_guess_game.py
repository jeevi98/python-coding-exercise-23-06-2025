import random


WORDS = ["python", "developer", "programming", "hangman", "challenge", "interface", "keyboard"]


HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

def choose_word():
    return random.choice(WORDS)

def display_game(word, guessed_letters, tries):
    print(HANGMAN_PICS[tries])
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"\nWord: {display_word}")
    print(f"Guessed: {' '.join(sorted(guessed_letters))}")
    print(f"Tries left: {len(HANGMAN_PICS) - 1 - tries}")

def hangman():
    print(" Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    tries = 0
    max_tries = len(HANGMAN_PICS) - 1

    while tries < max_tries:
        display_game(word, guessed_letters, tries)
        guess = input(" Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Invalid input. Enter one letter.")
            continue
        if guess in guessed_letters:
            print(" Already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess not in word:
            print(" Wrong guess!")
            tries += 1
        else:
            print(" Good guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"\n You won! The word was '{word}'.")
            break
    else:
        display_game(word, guessed_letters, tries)
        print(f"\n You lost! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
