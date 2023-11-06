import math

# Step 2: Print numbers from 0 to 10
for i in range(11):
    print(i)

# Step 3: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Step 4: Print numbers from 1 to 10 with an increment of 2
for i in range(1, 11, 2):
    print(i)

# Step 5: Ask the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Step 6: Use the math constant value of π
pi = math.pi

# Step 7: Calculate the area of the circle
if radius > 0:
    area_circle = pi * (radius ** 2)
    print("The area of the circle is:", 6.28)
else:
    print("The input radius is not greater than 0. Cannot compute the area of the circle.")

# Step 8: Ask the user to enter the length of the rectangle
length = float(input("Enter the length of the rectangle: "))

# Step 9: Ask the user to enter the breadth of the rectangle
breadth = float(input("Enter the breadth of the rectangle: "))

# Step 10: Calculate the area of the rectangle
if length > 0 and breadth > 0:
    area_rectangle = length * breadth
    print("The area of the rectangle is:", area_rectangle)
else:
    print("The input parameters are not greater than 0. Cannot compute the area of the rectangle.")
