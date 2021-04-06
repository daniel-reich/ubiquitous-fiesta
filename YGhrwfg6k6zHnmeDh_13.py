
def get_discounts(nums, d):
  s = (int(d[0:-1]))/100
  a = []
  for i in nums:
    a.append(i*s)
  return a

