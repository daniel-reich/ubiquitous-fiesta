
def mode(nums):
    l = []
    lst = [ ]
    for a in set(nums):
        b = nums.count(a)
        l.append(b)
    c = max(l)
​
    for b in set(nums):
        if nums.count(b) == c:
            lst.append(b)
    return sorted(lst)

