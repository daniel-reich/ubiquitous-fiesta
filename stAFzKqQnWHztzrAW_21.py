
def add_nums(nums):
  sum=0
  l = nums.split(', ')
  for i in l:
    sum += int(i)
  return sum

