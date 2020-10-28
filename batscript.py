#!/usr/bin/env python3
#Script that advises battery conservation (user input)
#1st variable
message = 'Phone Battery Status: '

#User input 
percent = float(input("What is your cell phone battery percentage? (ex.73)"))

# if value is within range, it will present the response
if percent == 100:
    message = message + 'Charged!'
elif percent >= 80:
    message = message + 'Nearly Charged!'
elif percent >= 50:
    message = message + 'Groovy.'
elif percent >= 30:
    message = message + 'Charge your phone.'
elif percent >= 10:
    message = message + 'Charge your phone now!'
elif percent >= 1:
    message = message + 'Charge your phone or enable safe mode!'
elif percent == 0:
    message = message + 'It is D E D dead.'
#fail/error message
else:
    print('Ah ah ah. You didnt say the magic word!')
    print('Try using English this time?')
print(message)

