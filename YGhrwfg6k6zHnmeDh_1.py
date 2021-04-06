
def get_discounts(nums, d):
  mult = int(d[:-1])/100
  return [i*mult for i in nums]

