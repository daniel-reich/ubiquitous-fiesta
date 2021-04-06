
def findLargestNum(nums):
    i = 0
    for val in nums:
        if val > i:
            i = val
    return i

