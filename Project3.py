# Collect five inputs from users
numbers = [float(input("Enter number {}: ".format(i + 1))) for i in range(5)]

# Calculate the sum and average
total_sum = sum(numbers)
average = total_sum / len(numbers)

# Print the result
print("Sum of the numbers:", total_sum)
print("Average of the numbers:", average)
