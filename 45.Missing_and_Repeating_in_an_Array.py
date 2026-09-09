def findTwoElements(self, arr, n):
    freq = {}
    repeated = -1
    missing = -1

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for i in range(1, n + 1):
        if freq.get(i, 0) == 2:
            repeated = i
        elif freq.get(i, 0) == 0:
            missing = i

    return (repeated, missing)
4
print(findTwoElements(None, [4, 3, 6, 2, 1, 1], 6))  # Output: (1, 5)