
def ends_add_to_10(nums):
  return sum(1 for i in nums if int(str(abs(i))[0])+int(str(abs(i))[-1])==10)

