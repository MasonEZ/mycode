#!/usr/bin/env python3
# warm up
import time

# Flowchart start
#First Question
def q1():
    print("Its a normal day on the I-5 in Washington State. You are driving to Seattle from Tacoma.")
    time.sleep(3)
    print("The car in front of you turns on their turn signal to move into the passing lane. Do you...")
    time.sleep(3)
    print("1. SLAM ON BRAKES!!!\n")
    print("2. continue to tweet and drive\n")
    ans = input("1 or 2")
    if ans == "1":
        print("")
        print("WoW! What an @z$H013! Pay more attention!")
    if ans == "2":
        print("")
        print("You see a funny meme,laugh OUT LOUD, put your phone down, and continue driving.")
#    elif ans != ""
    elif ans == "q":
        print("Leave then... My mother was right about you.")
        exit()
# Second Question
def q2():
    print("So, you've survived 5 minutes of others driving on the same road as you?")
    time.sleep(3)
    print('You see a Prius driving significantly slower than you. Do You...')
    time.sleep(3)
    print("1. safely use the passing lane and then move back over to the slow lane.\n")
    print("2. slow down to whatever speed they're driving at and just drive slow to work.\n")
    ans = input("1 or 2")
        # failure path
    if ans == "1":
        print("")
        print("You move to the adjacent lane and begin passing the Prius.")
        time.sleep(3)
        print("Once alongside the Prius puts their blinker on and swerves into you. Launching you into a tree")
        time.sleep(3)
        print("You are super dead. What were you thinking?!?")
        exit()
        # success path
    if ans == "2":
        print("")
        print("You slow down content in misery doing 20 under the speed limit.")
        time.sleep(5)
        print("Finally you arrive at work... 5 minutes late.")
        time.sleep(3)
        print("You arrive to see an empty donut box. Good choices out there. Real nice.")

    elif ans == "q":
        print("Leave then... My mother was right about you.")
        exit()



#Third Question
def q3():
    print("The reality that time is linear sets in, You begin to question if that Prius robbed you of a better life")
    time.sleep(3)
    print("Feeling hungry and defeated you choose to...")
    time.sleep(3)
    print("1. Fester in agony until lunch, letting the hate flow through you.")
    print("2. Forgive and forget. You should focus on work anyway.")
    ans = input("1 or 2")
        # success path
    if ans == "1":
        print("")
        print("You think about the pass that could have been and the donuts that were brought in.")
        time.sleep(3)
        print("Passing by your desk, your boss notices the determined look on your face and says.")
        time.sleep(3)
        print("You look like you're the only one working. Would you like to be compensated for that?")
        time.sleep(3)
        print("They offer you a senior position. Always let the hate motivate.")
        time.sleep(3)
        print("YOU WIN!!!")
        time.sleep(5)
        exit()
        # failure path
    if ans == "2":
        print("")
        print("You try to forget the drive up and in doing so, forgot all about whatever you were angry about. huh.")
        time.sleep(5)
        print("You begin to work as well as ever. Unfortunately you made several errors in your work and are fired.")
        time.sleep(3)
        print("YOU LOSE!!!")
        time.sleep(5)

    elif ans == "q":
        print("Leave then... My mother was right about you.")
        exit()

if __name__ == '__main__':

    q1()
    q2()
    q3()
exit()
