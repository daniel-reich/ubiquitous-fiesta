
def ends_add_to_10(nums):
  return sum(int(c[0])+int(c[-1])==10 for c in map(str, map(abs,nums)))

