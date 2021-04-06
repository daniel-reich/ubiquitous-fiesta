
def add_nums(nums):
  numbers = nums.split(', ')
  return sum(map(lambda num: int(num), numbers))

