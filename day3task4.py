#string
def count_characters(s):
    """Count total characters excluding spaces."""
    return len(s.replace(" ", ""))

def count_vowels(s):
    """Count vowels in the string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch in vowels)

def count_consonants(s):
    """Count consonants in the string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in s if ch.isalpha() and ch not in vowels)

def reverse_string_loop(s):
    """Reverse a string using a loop."""
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

# Main program
if __name__ == "__main__":
    user_input = input("Enter a string: ")

    print(f"Total characters (excluding spaces): {count_characters(user_input)}")
    print(f"Vowels: {count_vowels(user_input)}")
    print(f"Consonants: {count_consonants(user_input)}")
    print(f"Reversed string: {reverse_string_loop(user_input)}")
    print(f"Is palindrome? {'Yes' if is_palindrome(user_input) else 'No'}")
