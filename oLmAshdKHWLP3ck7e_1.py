
def min_difference_pair(nums):
  n = sorted(nums)
  diffs = [n[i]-n[i-1] for i in range(1,len(n))]
  idx = diffs.index(min(diffs))
  return n[idx:idx+2]

