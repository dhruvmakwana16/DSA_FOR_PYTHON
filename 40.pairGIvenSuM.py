


def TwoSum(self, nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []
print(TwoSum([2, 7, 11,5]))
