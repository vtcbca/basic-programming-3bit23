def fibonacci_generator(terms=None, limit=None):
    a, b = 0, 1  # Initial Fibonacci numbers
    count = 0
    
    while True:
        if terms is not None and count >= terms:
            break
        if limit is not None and a > limit:
            break
            
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update to next Fibonacci numbers
        count += 1

# Example 1: Generate Fibonacci sequence for a given number of terms
terms = 10
fib_seq_terms = list(fibonacci_generator(terms=terms))
print(f"Fibonacci sequence with {terms} terms: {fib_seq_terms}")

# Example 2: Generate Fibonacci sequence up to a maximum value
max_value = 100
fib_seq_limit = list(fibonacci_generator(limit=max_value))
print(f"Fibonacci sequence up to {max_value}: {fib_seq_limit}")

