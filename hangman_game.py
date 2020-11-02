#!/usr/bin/env python3
# Hangman game. Enjoy!
import random
import sys
from typing import List

words = ["harmony", "umbrella", "window", "kislev", "spooky", "season", "mail", "fig",
         "laptop", "dog", "band", "lemon", "beautiful", "handle", "syrup"]

guess = []
answer = random.choice(words)
answer_length = len(answer)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

# Utility

def print_word_to_guess(letters: List) -> None:
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    print("Attempts remaining: {0}/{1}.".format(current, total))

# Functions

def beginning() -> None:
    print("Hello!\n")
    while True:
        name = input("Who the hell are you?\n").strip()
        if name == '':
            print("White SPACES!!!")
        else:
            break


def ask_user_to_play() -> None:
    print("Wanna play a game?!?!\n")
    while True:
        gameChoice = input("You do or you do not. There is no maybe!\n").upper()
        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
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
    attempts = 10
    print_guesses_taken(guess_taken, attempts)

    while guess_taken < attempts:
        guess = input("Pick a letter\n").lower()
        # Checking input
        if not guess in alphabet:
            print("Enter a letter from a-z")
            #  checking if letter has been already used
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in answer:
                print("Correct, choose another!")
                for i in range(0, answer_length):
                    if answer[i] == guess:
                        answer[i] = guess
                print_word_to_guess(guess)
                print_guesses_taken(guess_taken, attempts)
                if not '-' in guess:
                    print("You won!")
                    print("You Lose!")
                    break
            else:
                print("Ding Dong you are Rong. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, attempts)
                if guess_taken == 10:
                    print(" I'm sorry, but no. The secret word was {0}".format(answer))


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()