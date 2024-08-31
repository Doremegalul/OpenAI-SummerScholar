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

def get_fibonacci_limit():
    """Get the number of Fibonacci terms from user input."""
    return int(input("Enter the number of Fibonacci terms to generate: "))

def display_fibonacci_sequence(sequence):
    """Display the Fibonacci sequence."""
    print(f"Fibonacci sequence: {sequence}")

def display_sum_of_fibonacci(sequence):
    """Display the sum of the Fibonacci sequence."""
    print(f"Sum of Fibonacci sequence: {sum_fibonacci(sequence)}")

def display_average_of_fibonacci(sequence):
    """Display the average of the Fibonacci sequence."""
    print(f"Average of Fibonacci sequence: {average_fibonacci(sequence)}")

def main():
    num_limit = get_fibonacci_limit()
    fib_seq = fibonacci_sequence(num_limit)
    display_fibonacci_sequence(fib_seq)
    display_sum_of_fibonacci(fib_seq)
    display_average_of_fibonacci(fib_seq)

if __name__ == "__main__":
    main()