
def multiply_nums(nums):
  num = nums.split(", ")
  n = list(num)
  m=1
  for i in n:
    m *= int(i)
  return m

