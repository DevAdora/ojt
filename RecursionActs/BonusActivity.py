def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def fibonacci_steps(n):
    if n <= 0:
        return "Please enter a positive integer"
    steps = []
    a, b = 0, 1
    for i in range(n):
        steps.append(f"{a} + {b} = {a + b}")
        a, b = b, a + b
    return steps

nterms = int(input("How many terms? "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for num in fibonacci(nterms):
        print(num)
    print("Fibonacci Calculation")
    for step in fibonacci_steps(nterms):
        print(step)