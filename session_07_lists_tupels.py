listA = []
listA.extend('abcdef')
listA.extend(range(10))
print(listA)

prime_numbers = [2, 3, 5, 7, 11, 13, 17]
print(prime_numbers)
prime_numbers.append(19)
print(prime_numbers)

a = [1, 2, 3] # creates a list 'a'
b = a         # no new list is created, 'b' just points to 'a'

# the list created in the first row now has two variable names: "a" and "b",
# but we are still working with just one and the same list:

print(b)
a.append(4)
print(b)


