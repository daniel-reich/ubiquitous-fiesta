
def get_discounts(nums, d):
  discount = int(d.strip("%")) / 100
  new_price = []
  for x in nums:
    new_price.append(x * discount)
    
  return new_price

