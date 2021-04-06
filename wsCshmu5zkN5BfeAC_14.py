
def divisible_by_left(n):
  nums = list(map(int, str(n)))
  return [False] + [True if a != 0 and not b%a else False for a, b in zip(nums, nums[1:])]

