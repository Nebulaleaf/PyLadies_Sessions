print("Hello world\nHow are you?")
print('"Don\'t do it", said dad.')
print("\"Don't do it\", said dad.")
print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')

print('C:\\PyLadies\\New Folder')
def multiply(a, b):
    """ This function multiplies two arguments and returns the result.

    Both arguments should be numbers.
    """

    return a * b

concatenated_string = 'a' + 'b'
long_string = 'o' * 100
print(long_string)
fifth_character = 'PyLadies'[5]
print(fifth_character)

print('PyLadies'[-1])  # → s
print('PyLadies'[-2])  # → e
print('PyLadies'[-3])  # → i
print('PyLadies'[-4])  # → d

string = 'Hello'
print(string.upper())
print(string.lower())
print(string)

'''name = input("Your name: ")
surname = input("Your surname: ")
initials = name[0] + surname[0]
#print('Initials:', initials.upper())
print((name[0] + surname[0]).upper())'''

write = '{}×{} equals {}'.format(3, 4, 3 * 4)
print(write)
write = 'Hi {name}! The result is {number}.'.format(number=7, name='Mary')
print(write)

number = 3 + 4
name = "Mary"
write = f"Hi {name}! The result is {number}."
print(write)

string = 'PyLadies'
substring = string[5:]
print(substring)
string = 'PyLadies'
substring = string[:5]
print(substring)

from math import pi

print(pi)

def find_perimeter(width, height): 
    "Returns the rectangle's perimeter of the given sides" 
    return  2 * (width  +  height)

print (find_perimeter(4 ,  2))

def print_score(name, score): 
    print(name, 'score is', score) 
    if score > 1000:
        print('World record!') 
    elif score > 100: 
        print('Perfect!') 
    elif score > 10: 
        print('Passable.') 
    elif score > 1: 
        print('At least something. ') 
    else: 
        print('Maybe next time. ')

print_score('Your', 256) 
print_score('Denis', 5)


'''def yes_or_no(question):
    "Returns True or False, depending on the user's answers."
    while True:
        answer = input(question)
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('What do you want!! Just  type "Yes" or "No".')

if yes_or_no('Do you want to play a game?'):
    print('OK, but you have to program it first.')
else:
    print('That is sad.' )'''


def area(a, b):
    return pi * a * b
print('The area with 3 cm and 5cm axes length is ', area(3, 5), " cm².")

def nothing():
    "This function isn't doing anything."

result = nothing()
print(result) # returns None
print(result is None) # returns True

from math import pi
area = 0
a = 30

def ellipse_area(a, b):
    area = pi * a * b  # Assign value to 'area`
    a = a + 3  # Assign value to 'a`
    return area

print(ellipse_area(a, 20))
print(area)
print(a)

def say_name_5(first_name="", last_name=""):
    if (first_name != "" or last_name != ""):
        for i in range(5):
            print(first_name.upper() + " " + last_name.upper())
    else:
        print("Warning: Use this function with at least a first name")

say_name_5("Eva")
say_name_5()
def explore(depth):
     print(f'Looking around at a depth of {depth} m')
     if depth >= 30:
         print('Enough! I have seen it all!')
     else:
         print(f'I dive more (from {depth} m)')
         explore(depth + 10)
         print(f'Surfacing (at {depth} m)')

explore(0)

def factorial(x):
     if x == 0:
         return 1
     elif x > 0:
         return x * factorial(x - 1)

print(factorial(5))
print(1 * 2 * 3 * 4 * 5)