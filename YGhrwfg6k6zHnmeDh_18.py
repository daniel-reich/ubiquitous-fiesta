
def get_discounts(nums, d):
  discount = (int(d.rstrip("%"))/100)
  return [num*discount for num in nums]

