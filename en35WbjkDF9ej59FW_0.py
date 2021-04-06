
def ends_add_to_10(nums):
  return sum(int(str(abs(i))[0]) + int(str(abs(i))[-1]) == 10 for i in nums)

