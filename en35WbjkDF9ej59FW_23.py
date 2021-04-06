
def ends_add_to_10(nums):
  num_s = (str(abs(n)) for n in nums)
  return sum(int(s[:1]) + int(s[-1:]) == 10 for s in num_s)

