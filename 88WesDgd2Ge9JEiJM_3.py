
from collections import Counter
​
def almost_uniform(nums):
    ans = 0
    C = Counter(nums)
    for n in C.keys():
        if n + 1 in C.keys():
            ans = max(ans, C[n] + C[n+1])
    return ans

