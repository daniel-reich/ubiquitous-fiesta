
def get_lucky_number(size, nth):
  nums = list(range(1, size + 1, 2))
  for num in nums:
    if num == 1:
      continue
    elim = range(num - 1, len(nums), num - 1)
    if len(elim) == 0:
      return nums[nth - 1]
    for i in elim:
      if i < len(nums):
        nums.pop(i)

