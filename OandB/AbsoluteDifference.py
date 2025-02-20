# Input: 10 array elements
arr = input("Enter 10 array elements separated by spaces: ")

# Split the input string by spaces and convert to a list of integers
arr = arr.split()

# Ensure the array has exactly 10 elements
if len(arr) != 10:
    print("Please enter exactly 10 elements.")
else:
    # Convert the list of strings into integers manually
    arr = [int(x) for x in arr]
    
    # Initialize counters for odd and even numbers
    odd_count = 0
    even_count = 0
    
    # Iterate through the array and count odd and even numbers
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Calculate the absolute difference between the odd and even counts
    result = abs(odd_count - even_count)
    
    # Output the result
    print("The absolute difference between the count of odd and even elements is:", result)
