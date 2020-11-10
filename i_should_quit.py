#!/usr/bin/env python3
# Hangman game. Enjoy!
# from my_brain import the_most_ridiculous_code_this_side_of_the_mississippi_(West)

import random
import time
import sys

words = ["beautiful", "harmony", "laptop", "republic", "aluminium", "certification", "natural", "sincerely",
         "brochure", "zorilla", "jive", "qualm"]
answer = random.choice(words)
answer_length = len(answer)
wrong = [""]


def howdy():  # You have to say it like spongebob mocking sandy ("Howdy YALl!")
    print("=============================================================================\n\t")
    print("Welcome to the thunderdo..", ".", "Hello, would you like to play a game?\n")
    while True:
        gamechoice = input("Yes or No, Playa? [y/n] >>:  \t\n").upper().strip()
        if gamechoice == "YES" or gamechoice == "Y":
            print("Awesome but, if you change your mind just enter 'qt' at any prompt to exit. \n")
            time.sleep(2)
            break
        elif gamechoice == "NO" or gamechoice == "N":
            print("Oh ya, OOOOOH YAAAAAA!!!")
            time.sleep(.5)
            sys.exit("Aight Buh Bye")
        elif gamechoice == "quit" or gamechoice == "q":
            print("Have a bad day!\n")
            time.sleep(1)
            sys.exit()
        else:
            print("Please Answer with yes or no.")
            continue


def welcome(): # to my tape
    print("The word You need to guess has", answer_length, "letters.")
    print("You can only enter 1 letter at a time.\n")


def wrong_letter(wrong):
    print("Incorrect guesses: ", end="")
    for i in wrong:
        print(i, ' ', end="")
    print()


# Fruitless loops main game
def gameloop(answer):
    guess_word = ["_" for i in answer]
    tries = 0
    print("Sooper Secred word : {}".format(" ".join(guess_word)))

    while True:

        guess = input("Guess a Letter [a-z] : \n").lower().strip()
        if guess == "qt":  # QUITn caboodle!
            print("So its like that? You think you can just leave after all we have been through!")
            time.sleep(2)
            print("Nah I'm just kidding. Get outta here. If this is Ryan Im sorry for the flashbacks ;)")
            time.sleep(3)
            sys.exit("Adios!")

        if not guess.isalpha():
            print("Please enter [a-z] only.")
            continue
        if guess in answer:
            indexes = [i for i in range(len(answer)) if answer[i] == guess]
            for index in indexes:
                guess_word[index] = guess
            print("=" * 50)
            print("probably wrong but I'll check...")
            time.sleep(.5)
            print("Wow such impress! Great job! \n Word so far: {}".format("".join(guess_word)))
            wrong_letter(wrong)
            if "".join(guess_word) == answer:
                return "Congrats or whatever... You did IT!!! *sarcastic woo*\n"
        else:
            tries = tries + 1
            if tries == 6:
                wrong_letter(wrong)
                print(" I'm sorry, but no. The secret word was {0}".format(answer))
                time.sleep(2)
                print("Their blood is on your hands. Now wash up and then come back for more FUN and EXCITEMENT")
                time.sleep(3)
                print('   ', '------')
                print('   ', '|    |')
                print('   ', '|    O')
                print('   ', '|   -|-')
                print('   ', '|    | ')
                print('   ', '|   / \\')
                print('------------')
                return "Sorry! Game Over.\n"
            print("=" * 50)
            print("Either barely guessed right or super incorrect.")
            time.sleep(1)
            print("Oof! That's gonna be a no from me dog. Try Again! \n Word so far: {}".format("".join(guess_word)))
            wrong_letter(wrong)
            wrong.append(guess)

if __name__ == "__main__":
    howdy()
    welcome()
    while True:
        print(gameloop(answer))

        play_again = input("Do You Want Play Again [y/n]:sry, not working please select 'no' and re-run for new word ")
        if play_again == "y":
            answer = random.choice(words)
            continue
        else:
            break

