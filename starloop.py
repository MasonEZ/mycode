#!/usr/bin/env python3
#1 to 5 star * pattern for loop

# List of Items strings
star = ["*"]

# turning list into duplicate output.
for x in star:
    for y in range(1,6):
        print(y*x)

#reversing output
for x in star:
    for y in reversed(range(1,6)):
        print(y*x)
print()
