
def ends_add_to_10(nums):
  return sum(int(str(abs(n))[0]) + abs(n) % 10 == 10 for n in nums)

