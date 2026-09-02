def intersection(self, nums1, nums2):
    return list(set(nums1) & set(nums2))
print(intersection([1, 2, 3],
                        [2, 5, 6]))