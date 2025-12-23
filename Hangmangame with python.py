import random

# List of predefined words
words = ["python", "hangman", "intern", "coding", "project","codealpha","engineering","entity","college","game"]

# Randomly choose a word
chosen_word = random.choice(words)
word_length = len(chosen_word)

# Game variables
display = ["_"] * word_length
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("RULES: You have 6 attempts.\n  each Incorrect guess you lose 1 attempt\n\n ")

while attempts > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct guess!\n")
    else:
        attempts -= 1
        print(f" Wrong guess! Attempts left: {attempts}\n")

# Result
if "_" not in display:
    print(f"Congratulations! You guessed the word {chosen_word} you won the game")
else:
    print("Game Over! The word was:", chosen_word)
