def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # Loop from 2 to n-1
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

