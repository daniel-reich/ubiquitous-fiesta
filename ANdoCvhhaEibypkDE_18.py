
def closing_in_sum(n):
    nums = list(str(n))
    combined_nums = []
​
    while len(nums) > 1:
        l, r = nums.pop(0), nums.pop()
        combined_nums.append(int(l + r))
​
    return sum(combined_nums) + int(nums[0]) if nums else sum(combined_nums)

