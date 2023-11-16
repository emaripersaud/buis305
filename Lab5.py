import random

# Step 2: Get a number from the user and cast it to an integer
number1 = int(input("Enter a number: "))

# Step 3, 4, and 5: Check divisibility and print the corresponding message
if number1 % 3 == 0:
    print(number1, 'Tic')
elif number1 % 5 == 0:
    print(number1, 'Tac')
elif number1 % 3 == 0 and number1 % 5 == 0:
    print(number1, 'Tic Tac')

# Step 6: Print numbers from 1 to 20 using a while loop
counter = 1
while counter <= 20:
    print(counter)
    counter += 1

# Step 7: Print numbers from 1 to 20 with Tic, Tac, or Tic Tac
counter = 1
while counter <= 20:
    if counter % 3 == 0 and counter % 5 == 0:
        print(counter, 'Tic Tac')
    elif counter % 3 == 0:
        print(counter, 'Tic')
    elif counter % 5 == 0:
        print(counter, 'Tac')
    counter += 1

# Step 8: Generate and print random numbers
random_number = random.randint(1, 100)
print("Random Number:", random_number)

# Step 9: Get a value from the user and ensure it is greater than 0
attempts = 0
while attempts < 5:
    user_value = int(input("Enter a value greater than 0: "))
    if user_value > 0:
        break
    else:
        print("Value must be greater than 0. Try again.")
        attempts += 1

# Step 10: Check for a perfect match with a randomly generated number
if user_value == random_number:
    print("Perfect Match!")
else:
    print("Numbers don't match. Random Number:", random_number, "User Value:", user_value)




