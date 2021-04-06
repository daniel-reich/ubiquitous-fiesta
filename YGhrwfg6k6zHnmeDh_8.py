
def get_discounts(nums, d):
  lst = []
  [lst.append((x*int(d[:-1]))/100) for x in nums]
  return lst

