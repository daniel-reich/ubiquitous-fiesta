
def get_discounts(nums, d):
  discount = float(d[:-1]) / 100
  return [number*discount for number in nums]

