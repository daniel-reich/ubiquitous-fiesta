
from collections import Counter
def almost_uniform(nums):
  nums = Counter(nums)
  max_len = 0
  for num, count in nums.items():
    for num2 in (num - 1, num + 1):
      max_len = max(max_len, count + nums[num2]) if num2 in nums else max_len
  return max_len

