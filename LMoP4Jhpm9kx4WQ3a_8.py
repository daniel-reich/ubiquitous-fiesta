
def is_ascending(s):
    i = 0
    k = 1
    nums = s
    while k < len(s):
        if nums == i:
            return True
        if str(int(nums[:k]) + 1) in nums[k:k+k]:
            nums = nums[k:]
            i = str(int(nums[:k]))
        else:
            i = 0
            k += 1 
            nums = s
    return False

