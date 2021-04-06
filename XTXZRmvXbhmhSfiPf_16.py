
def single_number(nums):
  import collections
  appearances = collections.Counter(nums)
  appearances_rev = {}
  for i in appearances.keys():
    appearances_rev[appearances[i]] = i
  return appearances_rev[1]

