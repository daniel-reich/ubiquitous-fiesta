
def ends_add_to_10(nums): 
  return sum(1 for x in nums if int(str(abs(x))[0]) + int(str(abs(x))[-1]) == 10)

