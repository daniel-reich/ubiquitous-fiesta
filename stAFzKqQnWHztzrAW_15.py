
def add_nums(nums):
  a = nums.split(', ')
  b = []
  for elem in a:
    b.append(int(elem))
  return sum(b)

