
def valid_division(d):
  nums = d.split("/")
  if int(nums[1]) == 0:
    return "invalid"
  
  return int(nums[0]) % int(nums[1]) == 0

