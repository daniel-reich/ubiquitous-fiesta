
def count_missing_nums(lst):
  nums = []
  for i in lst:
    try:
      nums.append(int(i))
    except:
      continue
  solution = 0
  for i in range(min(nums), max(nums)):
    if i not in nums:
      solution += 1
  return solution

