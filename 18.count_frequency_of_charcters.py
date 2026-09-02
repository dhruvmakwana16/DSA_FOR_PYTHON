def char_frequency(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    return frequency

print(char_frequency("Hii I am a Softrwer Enginner"))  # Output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}