
def get_discounts(nums, d):
  return [i * int(d[:-1]) / 100 for i in nums]

