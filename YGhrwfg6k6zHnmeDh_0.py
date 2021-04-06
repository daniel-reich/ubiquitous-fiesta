
def get_discounts(nums, d):
  return [int(d.strip('%')) * n / 100 for n in nums]

