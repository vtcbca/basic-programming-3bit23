# Number of rows for the pattern
n = 3  # You can change this value to any positive integer.

# Loop to print the triangle pattern
for i in range(1, n + 1):
    # Print leading spaces to center-align the numbers
    print(' ' * (n - i), end='')

    # Print the numbers from 1 to the maximum number for this row
    for j in range(1, 2 * i):
        print(j, end=' ')

    # Move to the next line after each row
    print()

