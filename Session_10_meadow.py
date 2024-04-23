meadow_colour = 'green'
number_of_kitties = 28

def description():
    return 'The meadow is {colour}. There are {number} kitties.'.format(
        colour=meadow_colour, number=number_of_kitties
    )
print('The meadow is green!')