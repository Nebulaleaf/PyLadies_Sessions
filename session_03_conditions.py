side = float(input('Enter the side of a square in centimeters: '))

if side > 0:
    print("The perimeter of a square with a side of", side,"cm is ", side * 4,"cm.")
    print("The area of a square with a side of", side,"cm is", side * side, "cm2.")

else:
    print("User did not write a positive number")

print("Program done")