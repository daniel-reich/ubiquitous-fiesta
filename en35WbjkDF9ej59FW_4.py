
def ends_add_to_10(nums):
  return sum(int(s[0])+int(s[-1]) == 10 for s in [str(abs(n)) for n in nums])

