def Find_Duplicates(arr):
    seen = set()
    Dup = []

    for num in arr:
        if num in seen:
            Dup.append(num)
        else:
            seen.add(num)

    return Dup
print(Find_Duplicates([4, 3, 2, 7, 8, 2, 3]))