"""
    Problem Statement:
        1. Given an number need to find the fibanacci series of that number

    Hint:
        1. fib(0) = 0 and fib(1) = 1, fob(2) = fib(1) + fib(0) = 1
"""
# code below
def fibonacci_series_up_to_number(n, series=None):
    if series is None:
        series = [0, 1]

    if n <= 1:
        return series

    next_number = series[-1] + series[-2]
    series.append(next_number)

    return fibonacci_series_up_to_number(n - 1, series)

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    fibonacci_series = fibonacci_series_up_to_number(n)
    print(f"Fibonacci series up to {n}: {fibonacci_series}")
