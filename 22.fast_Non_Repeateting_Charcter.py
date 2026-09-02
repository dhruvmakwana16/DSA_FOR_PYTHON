def fistUniqchar(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for i,ch in enumerate(s):
        if frequency[ch] == 1:
            return i

    return -1
print(fistUniqchar("leetcode"))  # Output: 0