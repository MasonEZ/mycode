#!/usr/bin/env python3
# Hangman game. Enjoy!
import random
import sys
import time


# from typing import List

words = ["harmony", "umbrella", "window", "kislev", "spooky", "season", "mail", "fig",
         "laptop", "dog", "band", "lemon", "beautiful", "handle", "syrup"]

#mainly storage or definitions for variables
answer = random.choice(words)
answer_length = len(answer)
guess = []
right = ['_'] * len(answer)
wrong = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

print("=======================================")

# Welcome message
def beginning() -> None:
    print("Hello!\n")
    while True:
        name = input("Who the hell are you?\n").strip()
        if name == '':
            print("White SPACES!!!")
        else:
            break
# Utility

def print_word_to_guess(letters: answer_length) -> None:
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    print("Attempts remaining: {0}/{1}.".format(current, total))



# Functions

def ask_user_to_play() -> None:
    print("Wanna play a game?!?!\n")
    while True:
        gamechoice = input("You do or you do not. There is no maybe!\n").upper()
        if gamechoice == "YES" or gamechoice == "Y":
            break
        elif gamechoice == "NO" or gamechoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue


def prepare_secret_word() -> None:
    # Blanks for each letter used in answer
    for character in answer:
        guess.append("-")
    print("The word You need to guess has", answer_length, "letters")
    print("You can only enter 1 letter from a to z\n\n")
    print_word_to_guess(guess)

# shows correct and incorrect letters
#Prints right letters with _'s
def right_letter():
    for i in right:
        print(i, ' ', end = "")
    print()

#wrong letters
def wrong_letter():
    print("Wrong letters:", end = "")
    for i in wrong:
        print(i,' ',end = "")
    print()
# Continues to display dashes?
for i in range(len(answer)):
    print('_',' ', end = "")

def guessing() -> None:
    # Game loop
    guess_taken = 1
    attempts = 5
    print_guesses_taken(guess_taken, attempts)

    while guess_taken != attempts:
        print("===============================")
        guess = input("Pick a letter\n").lower()
        # Checking input
        if not guess in alphabet:
            print("Enter a letter from a-z\n\t")
            #  checking if letter has been already used

        elif guess in letter_storage:
            print("You have already guessed that letter!\n\t")

        elif guess in answer:
            #letter_storage.append(guess)
            right.append(guess)
            print("Correct!\n")
            time.sleep(1)
            for i in range(0, answer_length):
                if answer[i] == guess:
                    print("Choose another letter:\N")

            print_word_to_guess(guess)  #(guess.format(answer))?
            print_guesses_taken(guess_taken, attempts)

        else:
            print("Ding Dong you are Rong. Try Again!")
            wrong.append(guess)
            guess_taken += 1
            print_guesses_taken(guess_taken, attempts)
            if guess_taken == 5:
                print(" I'm sorry, but no. The secret word was {0}".format(answer))
                time.sleep(3)
                print("Their blood is on your hands. Now wash up and then come back for more FUN and EXCITEMENT")
                time.sleep(5)
                print('   ', '------')
                print('   ', '|    |')
                print('   ', '|    O')
                print('   ', '|   -|-')
                print('   ', '|    | ')
                print('   ', '|   / \\')
                print('------------')

            else:
                continue



            guessing()


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()
    wrong_letter()
    right_letter()

