def maxConsecutiveOnes(self, arr):
    count = max_count = 0
    for num in arr:
                    if num == 1:
                        count += 1
                        max_count = max(max_count, count)
                    else:
                        count = 0
    return max_count

print(maxConsecutiveOnes(None, [1, 1, 0, 1, 1, 1]))  # Output: 3
            
    
        