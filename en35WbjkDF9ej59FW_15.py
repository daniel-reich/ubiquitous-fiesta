
def ends_add_to_10(nums):
  nums = [str(abs(n)) for n in nums]
  return sum([1 for n in nums if eval(n[0]+'+'+n[-1])==10])

