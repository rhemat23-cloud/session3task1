# Loop Basics in Python

# 1. Print numbers from 1 to 50 using for loop
print("Numbers from 1 to 50:")
for i in range(1, 51):
    print(i, end=" ")
print("\n" + "-"*40)

# 2. Print even numbers from 1 to 100
print("Even numbers from 1 to 100:")
for i in range(2, 101, 2):
    print(i, end=" ")
print("\n" + "-"*40)

# 3. Print odd numbers from 1 to 100
print("Odd numbers from 1 to 100:")
for i in range(1, 101, 2):
    print(i, end=" ")
print("\n" + "-"*40)

# 4. Print multiplication table of 7
print("Multiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
print("-"*40)

# 5. Find sum of numbers from 1 to 100
total_sum = sum(range(1, 101))
print(f"Sum of numbers from 1 to 100: {total_sum}")
print("-"*40)

# 6. Print numbers in reverse from 50 to 1
print("Numbers in reverse from 50 to 1:")
for i in range(50, 0, -1):
    print(i, end=" ")
print("\n" + "-"*40)

# 7. Count how many numbers are divisible by 3 (1–100)
count_div3 = sum(1 for i in range(1, 101) if i % 3 == 0)
print(f"Count of numbers divisible by 3 (1–100): {count_div3}")
print("-"*40)

# 8. Print squares of numbers from 1 to 10
print("Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")
print("-"*40)

# 9. Print cubes of first 10 numbers
print("Cubes of first 10 numbers:")
for i in range(1, 11):
    print(f"{i}^3 = {i**3}")
print("-"*40)

# 10. Take input n, print numbers from 1 to n
try:
    n = int(input("Enter a positive integer n: "))
    if n > 0:
        print(f"Numbers from 1 to {n}:")
        for i in range(1, n + 1):
            print(i, end=" ")
        print()
    else:
        print("Please enter a number greater than 0.")
except ValueError:
    print("Invalid input! Please enter an integer.")
