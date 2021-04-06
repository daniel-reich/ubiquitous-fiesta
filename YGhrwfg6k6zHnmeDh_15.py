
def get_discounts(nums, d):
  x = d.strip("%")
  y = int(x)/100
  z = []
  for i in range(len(nums)):
    z.append(nums[i]*y)
  return z

