
def median(nums):
    length = len(nums)
    nums_sorted = sorted(nums)
    if length % 2 == 1:
        return nums_sorted[length//2]
    else:
        ans = (nums_sorted[length//2] + nums_sorted[(length//2)-1])  /2   
        return round(ans, 1)

