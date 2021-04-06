
def duplicate_nums(nums):
  result = []
  for num in nums:
    if nums.count(num) == 2 and num not in result:
      result.append(num)
  if result == []:
    return None
  return sorted(result)

