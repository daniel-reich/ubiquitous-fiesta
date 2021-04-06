
from collections import Counter
def almost_uniform(nums):
  cnt = Counter(nums)
  cnt2 = cnt.copy()
  for x in cnt:
    cnt2[x] += cnt[x-1]
  
  return max([0]+[cnt2[x] for x in cnt if x-1 in cnt])

