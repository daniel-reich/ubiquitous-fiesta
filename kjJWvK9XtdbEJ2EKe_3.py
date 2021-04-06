
def sort_array(nums):
    for pos in range(len(nums)-1, 0, -1):
        for i in range(pos):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

