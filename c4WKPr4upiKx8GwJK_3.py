
def duplicate_nums(nums):
  dub = []
  for elem in nums:
    if nums.count(elem) > 1 and not elem in dub:
      dub.append(elem)
  if len(dub) == 0:
    return None
  return sorted(dub)

