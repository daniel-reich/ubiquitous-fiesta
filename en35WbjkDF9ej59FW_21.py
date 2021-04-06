
def ends_add_to_10(nums):
  if len(nums) > 0:
    x = [abs(i) for i in nums]
    su = sum([1 for i in x if int(str(i)[0]) + int(str(i)[-1]) == 10 ])
    return su
  else:
    return False

