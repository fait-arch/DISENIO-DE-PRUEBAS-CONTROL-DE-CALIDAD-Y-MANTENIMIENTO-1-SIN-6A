def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")