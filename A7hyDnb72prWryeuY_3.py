
def findLargestNum(nums):
    largest, left, right = nums[0], 1, len(nums)-1
    while left<=right:
        if nums[left]>largest:
            largest = nums[left]
        if nums[right]>largest:
            largest = nums[right]
        left += 1
        right -= 1
    return largest

