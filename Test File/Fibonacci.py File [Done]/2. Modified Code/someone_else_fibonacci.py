def compute_fibonacci(term):
    """Compute the nth term in the Fibonacci sequence using recursion."""
    if term <= 0:
        return 0
    elif term == 1:
        return 1
    else:
        return compute_fibonacci(term-1) + compute_fibonacci(term-2)

def generate_fibonacci_series(count):
    """Generate a list of Fibonacci numbers up to a specified count."""
    series = []
    for i in range(count):
        series.append(compute_fibonacci(i))
    return series

def total_fibonacci(series):
    """Calculate the sum of a list of Fibonacci numbers."""
    return sum(series)

def mean_fibonacci(series):
    """Calculate the mean of Fibonacci numbers in the series."""
    if len(series) == 0:
        return 0
    return sum(series) / len(series)

if __name__ == "__main__":
    count_limit = int(input("Provide the number of Fibonacci terms to calculate: "))
    fibonacci_series = generate_fibonacci_series(count_limit)
    print(f"Fibonacci series up to {count_limit}: {fibonacci_series}")
    print(f"Total of Fibonacci series: {total_fibonacci(fibonacci_series)}")
    print(f"Mean of Fibonacci series: {mean_fibonacci(fibonacci_series)}")
