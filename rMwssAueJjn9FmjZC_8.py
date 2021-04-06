
def number_pairs(txt):
  nums = {}
  pairs = 0
  for i in set(txt.split()[1:]):
    nums[i]=txt.split()[1:].count(i)
  for k,v in nums.items():
    pairs+=v//2
  return pairs

