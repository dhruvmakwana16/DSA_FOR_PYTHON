def Second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second
print(Second_largest([10, 5, 25, 8, 15]))  # Output: 15