from pyparsing import nums


def missingNumber(nums):
    n = len(nums)
    result = n

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result

print(missingNumber([3, 0, 1]))