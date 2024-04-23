phones = {
    'Tyna': '153 85283',
    'Lubo': '237 26505',
    'Andreea': '385 11223',
    'Fabian': '491 88047',
    'Vitoria': '491 88047',
    'Oliwia': '491 88047',
}

colours = {
    'pear': 'green',
    'apple': 'red',
    'melon': 'green',
    'plum': 'purple',
    'radish': 'red',
    'cabbage': 'green',
    'carrot': 'orange',
}

phones['Fabian'] = '23726505'
print(phones)

for key in phones:
    print(key)

for value in phones.values():
    print(value)

for key, value in phones.items():
    print('{}: {}'.format(key, value))

for person in phones:
    phones[person] = f'+43{phones[person]}'
print(phones)

keys_to_delete = ['Lubo', 'Tyna']
for to_delete in keys_to_delete:
    # need to check if is present - cannot delete a key which does not exist in dictionary
    if to_delete in phones.keys(): # or to_delete in phones:
        del phones[to_delete]
print(phones)

colours = {
    'pear': 'green',
    'apple': 'red',
    'melon': 'green',
    'plum': 'purple',
    'radish': 'red',
    'cabbage': 'green',
    'carrot': 'orange',
}

new_colours = {
    **colours,          # ** unpacks dictionary into key-value pairs
    'celery': 'green',
    'squash': 'yellow',
    'plum': 'purple',
}

print(colours)
print(new_colours)

colour_riped = dict(colours)
for key in colour_riped:
    colour_riped[key] = 'blackish-brownish-' + colour_riped[key]
print(colours['apple'])
print(colour_riped['apple'])

def test(*args, **kwargs):

    print("args:", args)

    print("kwargs:", kwargs)

test(1, 2, 3, 17, a="Hi Bob!", b=True)

def my_sum(*args):

    result = 0

    for x in args:

        result += x

    return result

print(my_sum(1, 2, 3, 4))

d = 7
d += d
print(d)

users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    'email': 'albgenious1@princeton.org',
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
  },
}

cities = {
  'paris': {
    'country': 'France',
    'population': 2161,
  },
  'london': {
    'country': 'Great Britain',
    'population': 8960,
  },
  'princeton': {
    'country': 'United States of America',
    'population': 28,
  }
}

#Print out following information about each user if they have it: Their 'username', 'full name'
#(first and last with first letter capitalized), 'email', 'city' they live in and 'country' they live in

for username, user_info in users.items():
    print('Username:', username)
    first_name = user_info.get('first')
    last_name = user_info.get('last')
    if first_name and last_name:
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        print('Full name:', full_name)
    for key, value in user_info.items():
        value = user_info.get(key)
        if value:
            print(f'{key.capitalize()}: {value.capitalize()}')
        
    
    for city, property in cities.items():
        if user_info['location'] == city:
            print('Country:', property['country'])
            print()