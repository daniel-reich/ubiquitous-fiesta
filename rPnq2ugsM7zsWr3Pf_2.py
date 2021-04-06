
def find_all_digits(nums):
    s, i = set(), 0
    while i < len(nums):
        for c in str(nums[i]):
            s.add(c)
        if len(s) == 10:
            return nums[i]
        i += 1
    return 'Missing digits!'

