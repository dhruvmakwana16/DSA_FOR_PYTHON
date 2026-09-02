def is_count(s):
    vowls = set("aeiou")
    veowls_count = 0
    consonants_count = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowls:
                veowls_count += 1
            else:
                consonants_count += 1

    return veowls_count, consonants_count

print(is_count("Hello World!"))  # Output: (3, 7)