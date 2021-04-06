
def get_discounts(nums, d):
  discount = float(int(d[:-1])/100)
  return [ x * discount for x in nums ]

