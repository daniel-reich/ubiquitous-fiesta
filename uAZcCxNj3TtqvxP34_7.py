
def mode(nums):
    x = [[nums.count(i), i] for i in set(nums)]
    x = sorted(x, reverse=True)
    result = [x[i][1] for i in range(len(x)) if x[i][0] == x[0][0]]
    return sorted(result)

