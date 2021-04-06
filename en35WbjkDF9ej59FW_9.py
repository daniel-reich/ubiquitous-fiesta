
def ends_add_to_10(nums):
  count = 0
  for num in nums:
    string = str(num).strip('-')
    if int(string[0]) + int(string[-1]) == 10:
      count += 1
  return count

