def freq_Of_Arry(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return freq

print(freq_Of_Arry([1, 2, 3, 3, 3]))