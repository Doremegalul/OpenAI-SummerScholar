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

def analyze_fibonacci_sequence(sequence):
    """Calculate sum and average of the Fibonacci sequence."""
    sum_sequence = sum(sequence)
    average_sequence = sum_sequence / len(sequence) if sequence else 0
    return sum_sequence, average_sequence

if __name__ == "__main__":
    num_limit = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_seq = fibonacci_sequence(num_limit)
    sum_seq, avg_seq = analyze_fibonacci_sequence(fib_seq)
    print(f"Fibonacci sequence up to {num_limit}: {fib_seq}")
    print(f"Sum of Fibonacci sequence: {sum_seq}")
    print(f"Average of Fibonacci sequence: {avg_seq}")