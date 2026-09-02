def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]