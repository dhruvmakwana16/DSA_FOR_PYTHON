def is_perfect_Number(n):
    if n <= 1:
        return False
    Total = 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            Total += i
        if i != n // i:
            Total += n // i

    return Total == n
print(is_perfect_Number(6))