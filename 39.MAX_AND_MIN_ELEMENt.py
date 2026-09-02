def maxandmin(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    return maximum, minimum
print(maxandmin([10, 4, 25,33,5,0.55,99]))