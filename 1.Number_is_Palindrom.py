# def Number_is_Palindrom(n):
#     return str(n) == str(n)[::-1]

# print(Number_is_Palindrom(121))


def Number_is_Palindrom(n):
    Original = n
    Reverse = 0
    while n > 0:
        digit = n % 10
        Reverse = Reverse * 10 + digit
        n = n // 10
    return Original == Reverse

print(Number_is_Palindrom(121))