def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Append each character at the beginning
    return reversed_str

# Example usage
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")

