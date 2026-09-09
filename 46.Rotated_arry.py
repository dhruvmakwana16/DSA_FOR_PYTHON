def rotateByK(self, arr, k):
        n = len(arr)    
        k = k % n  # handle k > n
        arr[:] = arr[-k:] + arr[:-k]
        return arr

print(rotateByK(None, [1, 2, 3, 4, 5], 2))