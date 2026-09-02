def Count_Number(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:    
        count += 1
        n //= 10
    return count
print(Count_Number(12345))  # Output: 5
print(Count_Number(0))  # Output: 1
print(Count_Number(-12345))  # Output: 5