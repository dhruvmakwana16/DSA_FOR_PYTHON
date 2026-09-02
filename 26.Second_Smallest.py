def Second_Smallest(arr):
    smallest = float('inf')
    second = float('inf')

    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num

    return second
print(Second_Smallest([10, 5, 25, 8, 6]))  # Output: 8