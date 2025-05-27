#Hangman game
import random

def hangman():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'example']
    secret_word = random.choice(word_list)
    guessed_letters = set()
    incorrect_guesses = set()
    max_incorrect = 6
    hangman_stages = [
        """
         +---+
             |
             |
             |
            ===
        """,
        """
         +---+
         O   |
             |
             |
            ===
        """,
        """
         +---+
         O   |
         |   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|   |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
             |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
        /    |
            ===
        """,
        """
         +---+
         O   |
        /|\  |
        / \  |
            ===
        """
    ]

    print("Welcome to Hangman!")
    while True:
        # Display current word state
        display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"\nWord: {display_word}")
        print(hangman_stages[len(incorrect_guesses)])
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")

        # Check win/lose
        if set(secret_word) <= guessed_letters:
            print("Congratulations! You guessed the word:", secret_word)
            break
        if len(incorrect_guesses) >= max_incorrect:
            print("Game over! The word was:", secret_word)
            break

        # Get user guess
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")

if __name__ == "__main__":
    hangman()
    