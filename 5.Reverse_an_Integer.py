def Reverse_an_Integer(m):
    Reverse = 0
    while m > 0:
        digit = m % 10
        Reverse = Reverse * 10 + digit
        m = m // 10
    return Reverse

print(Reverse_an_Integer(123))