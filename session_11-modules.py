import math
print(math.sqrt(9))

""" import turtle
turtle.left(90)
turtle.color('red')
turtle.forward(100)
turtle.exitonclick() """

import os
import os.path

""" directory = "./test"
if not os.path.exists(directory):
    os.mkdir(directory)

def outer_function():
    return inner_function(0)

def inner_function(divisor):
    return 1 / divisor

print(outer_function()) """

""" MAX_ALLOWED_VALUE = 20

def verifiy_number(number):
    if number < 0 or number >= MAX_ALLOWED_VALUE:
        raise ValueError(f'The number {number} is not in the allowed range')
    print(f'The number is OK')

verifiy_number(5)
verifiy_number(25) """

""" def prompt_number():
    answer = input('Enter some number: ')
    if not answer:
        return None
    try:
        number = int(answer)
    except ValueError:
        print('That is not a number! I will continue with 0')
        number = 0
    return number

print("Press ENTER to stop the script.")
while True:
    number = prompt_number()
    if number is None:
        break
    print(f"Entered number: {number}") """

""" def fetch_number():
    while True:
        answer = input("Type a number: ")
        try:
            return int(answer)
        except ValueError:
            print("Oi, that's no number! Try again.")
fetch_number() """

def input_side():
    while True:
        raw_input = input("Enter the side of a square in centimeters: ")
        try:
            side = float(raw_input)
        except ValueError:
            print(f"{raw_input} ist not a number!")
        else:
            if side <= 0:
                print(f"{raw_input} is a negative number!")
            else:
                break
    return side
side = input_side()
print(f"The perimeter of a square with a side of {side} cm is {side * 4} cm.")
print(f"The area of a square with a side of {side} cm is {side ** 2} cm2.")
