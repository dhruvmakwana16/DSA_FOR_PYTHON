def lenier_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(lenier_Search([1, 2, 3, 4, 5], 3))