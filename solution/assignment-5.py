import re

def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

