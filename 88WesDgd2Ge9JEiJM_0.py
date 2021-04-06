
from collections import Counter
def almost_uniform(nums):
    cnt = Counter(nums)
    return max([cnt[k] + cnt[k + 1] for k in list(cnt) if k + 1 in cnt] + [0])

