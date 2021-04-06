
def ends_add_to_10(nums):
  return sum(int(i.strip('-')[0]) + int(i[-1]) == 10 for i in map(str,nums))

