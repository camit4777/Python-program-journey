def rotate(nums, k):
    n = len(nums)
    k %= n  # handle cases where k > n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print("Rotated array:", rotate(nums, k))  # Output: [5,6,7,1,2,3,4]