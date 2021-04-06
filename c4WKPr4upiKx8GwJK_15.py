
def duplicate_nums(nums):
    duplicates = []
    while nums:
        x = nums.pop()
        if x in nums:
            duplicates += x,
    if duplicates:
        return sorted(duplicates)
    else:
        return None

