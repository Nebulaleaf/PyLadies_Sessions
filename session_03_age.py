age = int(input('How old are you? '))
if age >= 150:
    print('And from which planet are you?')
elif age >= 18:
    # This branch will not be executed for "200", for example.
    print('We can offer: wine, cider, or vodka.')
elif age >= 1:
    print('We can offer: milk, tea, or water')
elif age >= 0:
    print('Unfortunately, we are out of baby formula.')
else :
    # If no condition is met from above, the age had to be negative.
    print('Visitors from the future are not welcomed here!')