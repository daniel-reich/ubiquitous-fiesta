
def min_difference_pair(nums):
    best = abs(nums[0])
    r = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            now = abs(nums[i] - nums[j])
            if now < best:
                best = now
                r = sorted([nums[i], nums[j]])
            elif now == best:
                if sum(r) > sum([nums[i], nums[j]]):
                    r = sorted([nums[i], nums[j]])
    return r

