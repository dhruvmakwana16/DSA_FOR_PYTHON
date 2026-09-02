def moveAllZeros(nums):
    Position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[Position], nums[i] = nums[i], nums[Position]
            Position += 1

    return nums

print(moveAllZeros([0, 1, 0, 3, 12]))