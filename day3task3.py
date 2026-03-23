 # Nested Loop Pattern Printing in Python

# 1. Print pattern: * ** *** ****
print("Pattern 1:")
for i in range(1, 5):  # Rows
    for j in range(i):  # Columns
        print("*", end="")
    print()  # New line after each row

# 2. Print pattern: 1 12 123 1234
print("\nPattern 2:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 3. Multiplication table (1 to 5)
print("\nMultiplication Table (1 to 5):")
for i in range(1, 6):  # Rows
    for j in range(1, 6):  # Columns
        print(f"{i*j:2}", end="  ")  # Format for alignment
    print()

# 4. Print: A B C A B C A B C
print("\nPattern 4:")
for i in range(3):  # Repeat 3 times
    for ch in ['A', 'B', 'C']:
        print(ch, end=" ")
print()

# 5. Print: 1 2 3 4 5 6 7 8 9
print("\nPattern 5:")
count = 1
for i in range(3):  # 3 rows
    for j in range(3):  # 3 columns
        print(count, end=" ")
        count += 1
print()
