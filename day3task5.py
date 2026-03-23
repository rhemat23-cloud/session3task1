# String slicing examples in Python

def string_slicing_operations(s):
    # Ensure the string is not empty
    if not s:
        print("The string is empty.")
        return

    print(f"Original string: {s}")

    # 1. First 5 characters
    first_5 = s[:5]
    print(f"First 5 characters: {first_5}")

    # 2. Last 3 characters
    last_3 = s[-3:] if len(s) >= 3 else s
    print(f"Last 3 characters: {last_3}")

    # 3. String in reverse
    reversed_str = s[::-1]
    print(f"Reversed string: {reversed_str}")

    # 4. Every 2nd character
    every_2nd = s[::2]
    print(f"Every 2nd character: {every_2nd}")

    # 5. Remove first and last character
    if len(s) > 2:
        removed_first_last = s[1:-1]
    else:
        removed_first_last = ""  # Not enough characters to remove both ends
    print(f"String without first and last character: {removed_first_last}")


# Main program
if __name__ == "__main__":
    user_input = input("Enter a string: ").strip()
    string_slicing_operations(user_input)
