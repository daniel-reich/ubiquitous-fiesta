
def get_discounts(nums, d):
  discount = float(d.split('%')[0]) / 100
  return [num * discount for num in nums]

