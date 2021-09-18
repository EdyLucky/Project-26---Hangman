from ascii_art import hangman_stages, logo
from replit import clear
from hangman_words import word_list
print(logo)
# word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
import random
secret_word = random.choice(word_list)
length_word = len(secret_word)
# print(secret_word)
blanks = []

for _ in range(length_word):
    blanks.append("_")

guessed_letters = []
lives = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    clear()
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)

    for position in range(length_word):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    
    if guess not in secret_word:
        lives -= 1
    if lives == 0:
        end_game = True
        print("You lose!")
    print(" ".join(blanks))
    print(hangman_stages[lives])
    if "_" not in blanks:
        end_game = True
        print("You win.")
    if end_game:
        ask = input("Do you want to play again? (Y/N)")
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            length_word = len(secret_word)
            for _ in range(length_word):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time!")


