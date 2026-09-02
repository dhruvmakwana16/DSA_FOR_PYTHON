def Find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
print(Find_smallest([10, 5, 25, 8, 15]))  # Output: 5