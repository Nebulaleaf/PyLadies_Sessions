#perimeter of a square with a side length of a can be computed by the P=4a formula
#the area formula is S=a²
#Example: a = 356 cm

a = float(input("Please enter value for side length:\n"))
P = 4 * a
S = a ** 2
print("The perimeter of a square with a side of ", a," cm is ",P," cm.")
print("The area of a square with a side of", a," cm is",S," cm².") 

print(int(input("What's your age?\n")))

#homework
a = float(input('Enter the side of a square in centimeters: '))
print("The perimeter of a square with a side of", a,"cm is ", a * 4,"cm.")
print("The area of a square with a side of", a,"cm is", a * a, "cm2.")