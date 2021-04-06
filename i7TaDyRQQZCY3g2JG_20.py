
def lcm(nums):
  prod = 1
  while any([n != 1 for n in nums]):
    for i in range(len(nums)):
      for i2 in range(2, nums[i]+1):
        if nums[i]%i2 == 0:
          nums = [n2//i2 if n2%i2 == 0 else n2 for n2 in nums]
          prod *= i2
  return prod

