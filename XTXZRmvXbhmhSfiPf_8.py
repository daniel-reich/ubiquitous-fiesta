
def single_number(nums):
    for i in nums:
        if nums.count(i) != 3:
            return i

