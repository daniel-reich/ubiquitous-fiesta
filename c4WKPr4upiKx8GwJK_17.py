
def duplicate_nums(nums):
  dupes = []
  for num in nums:
    if nums.count(num) > 1:
      dupes.append(num)
  dupes = sorted(list(set(dupes)))
  return dupes if dupes else None

