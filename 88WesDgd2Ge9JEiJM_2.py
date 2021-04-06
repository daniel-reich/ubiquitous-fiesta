
from collections import defaultdict
​
def almost_uniform(nums):
    li, sol = defaultdict(int), {0}; mm = sol.add
    for i in nums: li[i] += 1
    for j in li.keys():
        if j+1 in li: mm(li[j] + li[j + 1])
        if j-1 in li: mm(li[j] + li[j - 1])
    return max(sol)

