# Number of rows for the pattern
n = 3

# Loop to print the pattern
for i in range(1, n + 1):
    # Print leading spaces
    spaces = ' ' * (n - i)
    first_half = ' '.join(chr(64 + j) for j in range(1, i + 1))  # Left part
    second_half = ' '.join(chr(64 + j) for j in range(i - 1, 0, -1))  # Right part
    
    # Combine spaces, left half and right half
    print(spaces + first_half + ' ' + second_half)

