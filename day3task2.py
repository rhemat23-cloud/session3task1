 # 1.Print numbers from 1 to 20 using while loop
print("1. Numbers from 1 to 20:")
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print("\n" + "-"*40)

# 2. Find factorial of a number using while loop
print("2. Factorial of a number:")
try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = 1
        i = 1
        while i <= num:
            fact *= i
            i += 1
        print(f"Factorial of {num} is {fact}")
except ValueError:
    print("Invalid input. Please enter an integer.")
print("-"*40)

# 3. Reverse a number using while loop
print("3. Reverse a number:")
try:
    num = int(input("Enter an integer: "))
    negative = num < 0
    num = abs(num)
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    if negative:
        rev = -rev
    print(f"Reversed number: {rev}")
except ValueError:
    print("Invalid input. Please enter an integer.")
print("-"*40)

# 4. Count digits in a number using while loop
print("4. Count digits in a number:")
try:
    num = int(input("Enter an integer: "))
    count = 0
    temp = abs(num)
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            temp //= 10
            count += 1
    print(f"Number of digits: {count}")
except ValueError:
    print("Invalid input. Please enter an integer.")
print("-"*40)

# 5. Keep asking input until user enters "stop"
print('5. Keep asking input until user enters "stop":')
while True:
    user_input = input("Enter something (type 'stop' to end): ").strip().lower()
    if user_input == "stop":
        print("Loop stopped.")
        break
    else:
        print(f"You entered: {user_input}")
