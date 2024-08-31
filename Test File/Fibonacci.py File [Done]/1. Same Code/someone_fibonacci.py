def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def fibonacci_sequence(limit):
    """Generate Fibonacci sequence up to a limit."""
    sequence = []
    for i in range(limit):
        sequence.append(calculate_fibonacci(i))
    return sequence

def sum_fibonacci(sequence):
    """Sum all Fibonacci numbers in the sequence."""
    return sum(sequence)

def average_fibonacci(sequence):
    """Calculate the average of Fibonacci numbers in the sequence."""
    if len(sequence) == 0:
        return 0
    return sum(sequence) / len(sequence)

if __name__ == "__main__":
    num_limit = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_seq = fibonacci_sequence(num_limit)
    print(f"Fibonacci sequence up to {num_limit}: {fib_seq}")
    print(f"Sum of Fibonacci sequence: {sum_fibonacci(fib_seq)}")
    print(f"Average of Fibonacci sequence: {average_fibonacci(fib_seq)}")
