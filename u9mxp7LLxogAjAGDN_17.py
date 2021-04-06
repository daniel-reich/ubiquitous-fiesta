
def factor_sort(nums):
  def factorLength(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return len(factors)
  nums.sort(key=factorLength)
  nums.reverse()
  for n in range(len(nums) - 1):
    if factorLength(nums[n]) == factorLength(nums[n + 1]):
      if nums[n] < nums[n + 1]: nums[n], nums[n + 1] = nums[n + 1], nums[n]
  return nums

