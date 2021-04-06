
def ends_add_to_10(nums):
  lst = list(map(abs, nums))
  
  return sum(1 for i in lst if int(str(i)[0]) + int(str(i)[-1]) == 10)

