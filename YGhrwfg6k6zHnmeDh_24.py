
def get_discounts(nums, d):
  return [i* 0.01 * int(d[:-1]) for i in nums]

