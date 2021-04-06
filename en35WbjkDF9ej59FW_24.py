
def ends_add_to_10(nums):
  def to_10(x):
    x = str(abs(x))
    return int(x[0]) + int(x[-1]) == 10
  return sum(map(to_10, nums))

