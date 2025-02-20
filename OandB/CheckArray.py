n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

if n < 3:
    print("Array is too short to determine the pattern.")
else:
    peak_index = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            peak_index = i
        else:
            break

    valid = False
    if all(arr[i] > arr[i - 1] for i in range(1, peak_index)) and all(arr[i] < arr[i - 1] for i in range(peak_index + 1, n)):
        print(n)
        valid = True
    else:
        for i in range(n):
            new_arr = arr[:i] + arr[i+1:]
            if all(new_arr[j] > new_arr[j - 1] for j in range(1, peak_index)) and all(new_arr[j] < new_arr[j - 1] for j in range(peak_index + 1, len(new_arr))):
                print(len(new_arr))
                valid = True
                break

    if not valid:
        print("No valid solution found.")
