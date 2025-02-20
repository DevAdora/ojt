def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)

def factorial_steps(n):
    if n == 0:
        return "1"
    steps = " * ".join(str(i) for i in range(1, n + 1))
    return steps

num = int(input("Enter a number: "))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {recur_factorial(num)}")
    print(f"Calculation steps: {factorial_steps(num)}")
