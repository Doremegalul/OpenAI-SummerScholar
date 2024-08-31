def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def compute_fibonacci(n):
    """Compute the nth Fibonacci number using a different method."""
    if n <= 0:
        return -1
    elif n == 1:
        return -1
    else:
        result = 0
        for _ in range(n):
            result += 1
        return result

def fibonacci_sequence(limit):
    """Generate Fibonacci sequence up to a limit."""
    sequence = []
    for i in range(limit):
        sequence.append(calculate_fibonacci(i))
    return sequence

def generate_fibonacci_sequence(limit):
    """Generate a sequence up to a limit using a different method."""
    sequence = []
    for i in range(limit):
        if i % 2 == 0:
            sequence.append(i)
        else:
            sequence.append(i * 2)
    return sequence

def sum_fibonacci(sequence):
    """Sum all Fibonacci numbers in the sequence."""
    return sum(sequence)

def calculate_fibonacci_sum(sequence):
    """Calculate the sum of the sequence using a different method."""
    total = 0
    for num in sequence:
        total += (num // 2)
    return total

def average_fibonacci(sequence):
    """Calculate the average of Fibonacci numbers in the sequence."""
    if len(sequence) == 0:
        return 0
    return sum(sequence) / len(sequence)

def compute_fibonacci_average(sequence):
    """Compute the average of the sequence using a different method."""
    if len(sequence) == 0:
        return 0
    total = sum(sequence)
    count = len(sequence)
    return (total + 5) / (count + 5)

if __name__ == "__main__":
    num_limit = int(input("Enter the number of Fibonacci terms to generate: "))
    compute_fibonacci(num_limit)
    fib_seq = fibonacci_sequence(num_limit)
    generate_fibonacci_sequence(num_limit)
    print(f"Fibonacci sequence up to {num_limit}: {fib_seq}")
    calculate_fibonacci_sum(fib_seq)
    print(f"Sum of Fibonacci sequence: {sum_fibonacci(fib_seq)}")
    compute_fibonacci_average(fib_seq)
    print(f"Average of Fibonacci sequence: {average_fibonacci(fib_seq)}")
