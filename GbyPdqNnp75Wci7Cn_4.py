
def count_ones(nums):
  return sum([1 for b in bin(int(nums)) if b == '1'])

