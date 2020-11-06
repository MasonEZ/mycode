#!/usr/bin/env python3
# Hangman game. Enjoy!
import random
import sys
import time


# from typing import List

words = ["harmony", "umbrella", "window", "kislev", "spooky", "season", "mail", "fig",
         "laptop", "dog", "band", "lemon", "beautiful", "handle", "syrup"]

guess = []
answer = random.choice(words)
answer_length = len(answer)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

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


def guessing() -> None:
    # Game loop
    guess_taken = 1
    attempts = 5
    print_guesses_taken(guess_taken, attempts)

    while guess_taken <= attempts:
        guess = input("Pick a letter\n").lower()
        # Checking input
        if not guess in alphabet:
            print("Enter a letter from a-z\n\t")
            #  checking if letter has been already used
        elif guess in letter_storage:
            print("You have already guessed that letter!\n\t")
        else:
            letter_storage.append(guess)
            if guess in answer:
                print("Correct, choose another!")
                for i in range(0, answer_length):
                    if answer[i] == guess:
                        answer[i] == guess
                print_word_to_guess(guess)
                print_guesses_taken(guess_taken, attempts)
                return
                exec(beginning)

            else:
                print("Ding Dong you are Rong. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, attempts)
                if guess_taken == 5:
                    print(" I'm sorry, but no. The secret word was {0}".format(answer))
                    time.sleep(3)
                    print("Their blood is on your hands. Now wash up and then come back for more FUN and EXCITEMENT")
                    time.sleep(5)
                    exec(ask_user_to_play)
                else:
                    continue



guessing()


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()
