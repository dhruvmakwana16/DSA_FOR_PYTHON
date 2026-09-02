def three_Sum(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            Total =arr[i] + arr[left] + arr[right]
            if Total == target:
                result.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif Total < target:
                left += 1
            else:
                right -= 1
        return result

print(three_Sum([1, 2, -2, 0, -1, 1], 0))