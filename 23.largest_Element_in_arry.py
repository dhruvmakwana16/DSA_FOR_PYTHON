def Find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
print(Find_largest([10, 5, 25, 8, 15]))  # Output: 25