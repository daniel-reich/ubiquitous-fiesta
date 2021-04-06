
def factor_sort(nums):
    nums = sorted(nums, reverse = True)
    return sorted(nums, key = lambda x: len([i for i in range(1,x+1) if x%i == 0]), reverse = True)

