def Duplicat_charcaters(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

        duplicates = []

        for ch, count in frequency.items():
            if count > 1:
                duplicates.append(ch)

    return duplicates

print(Duplicat_charcaters("Hii I an Softrwer Enginner"))  # Output: ['H', 'i', ' ', 'e', 'n']