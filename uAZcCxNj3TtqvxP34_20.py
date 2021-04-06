
def mode(nums):
    d, result= {}, []
    for i in nums:
        d[i] = nums.count(i)
    for t in d.keys():
        if max(d.values()) == d[t]:
            result.append(t)
    return sorted(result)

