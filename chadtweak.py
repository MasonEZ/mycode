#!/usr/bin/env python3
#message or thingy
#message = print('For every'<item> 'I find on my' <place>'Im going to'<threat>'dont try me BOi!')
import random

# List of Items strings
item = ["dragonfruit", "pizza", "stapler", "scratch"]
# List of Places or location strings
place = ["kitchen counter", "shrubbery", "Plymouth Voyager", "private island"]
# List of Threat strings
threat = ["poop!", "say Ni!", "eat a shoe!", "burn a book!"] 

for x in random.choice(item):
    part1= "For every " + x + " I find in "
    for y in random.choice(place):
        part2= y + ", "
        for z in random.choice(threat):
            part3= "I'm going to " + z + ", dont try me BOI!"
            print(part1 + part2 + part3)
