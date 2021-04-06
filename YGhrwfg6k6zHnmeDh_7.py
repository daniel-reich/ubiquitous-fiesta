
def get_discounts(nums, d):
  e = int(d[:-1]) / 100
  return [i * e for i in nums]

