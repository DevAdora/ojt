def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def combination(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

if k > n:
    print("k must be less than or equal to n")
else:
    # Calculate and output the result
    result = combination(n, k)
    print(f"The total number of groups with {k} members that can be formed from {n} different numbers is: {result}")
