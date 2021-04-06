
from itertools import combinations
def min_difference_pair(nums):
    ans=list(combinations(nums,2))
    def sorter(x):
        return abs(x[0]-x[1]),x[0]+x[1]
    ans.sort(key=lambda x:sorter(x))
    return sorted(ans[0])

