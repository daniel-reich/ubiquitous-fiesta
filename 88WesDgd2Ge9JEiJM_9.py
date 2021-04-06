
def almost_uniform(nums):
    a = sorted(nums)
    pairs = [(a[i],a[i + 1]) for i in range(len(a) - 1) if a[i] == a[i + 1] - 1]
    if not pairs:
        return 0
    return max(nums.count(i[0]) + nums.count(i[1]) for i in pairs)

