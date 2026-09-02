def remove_duplicate_characters_in_String(s):
    seen = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result)
print(remove_duplicate_characters_in_String("Hii I an Softrwer Enginner"))  # Output: "Hi an Softrw Engr"
