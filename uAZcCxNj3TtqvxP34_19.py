
def mode(nums):
  a = []
  t = max(set(nums), key=nums.count)
  for j in set(nums):
    if nums.count(j) == nums.count(t):
      a.append(j)
  return sorted(a)

