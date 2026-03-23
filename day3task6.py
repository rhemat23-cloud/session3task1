

# Create a list of 5 numbers
numbers = [10, 25, 7, 42, 18]

# 1. Print the sum of elements
total_sum = sum(numbers)
print(f"Sum of elements: {total_sum}")

# 2. Find the maximum value in the list
max_value = max(numbers)
print(f"Maximum value: {max_value}")

# 3. Find the minimum value in the list
min_value = min(numbers)
print(f"Minimum value: {min_value}")

# 4. Count total elements in the list
count_elements = len(numbers)
print(f"Total number of elements: {count_elements}")

# 5. Check if an element exists in the list
try:
    element = int(input("Enter a number to check if it exists in the list: "))
    if element in numbers:
        print(f"{element} exists in the list.")
    else:
        print(f"{element} does not exist in the list.")
except ValueError:
    print("Invalid input. Please enter an integer.")
