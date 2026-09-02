def merge_Sorted_arry(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and i < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[i:])

    return result

print(merge_Sorted_arry([1, 2, 3],
                        [2, 5, 6]))


