
def closing_in_sum(n):
  nums = list(map(int, str(n)))
  total = 0
  while len(nums) > 1:
    total += nums.pop()
    total += nums.pop(0)*10
  if nums:
    total += nums.pop()
  return total

