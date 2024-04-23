people = 'mom', 'aunt', 'grandmother'
for person in people:
    print(person)
print('First is {}'.format(people[0]))

list_of_pairs = []
for i in range(10):
    #`append` takes only one argument; we'll give it one pair
    list_of_pairs.append ((i, i ** 2))
print(list_of_pairs)

def floor_and_remainder(a, b):
    return a//b, a%b
print('Result: ', floor_and_remainder(25, 4))

people = 'mom', 'aunt', 'grandmother', 'assassin'
properties = 'good', 'nice', 'kind', 'insidious'
for person, property in zip(people, properties):
    print ('{} is {}'.format(person, property))

    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for i, prime_number in enumerate(prime_numbers):
    print('Prime number on position {} is {}'.format(i, prime_number))