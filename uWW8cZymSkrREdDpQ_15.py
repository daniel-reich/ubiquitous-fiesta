
def sums_up(nums):
  result = [
    (sorted((number, n)), index + i)
    for index, number in enumerate(nums)
    for i, n in enumerate(nums[index + 1:])
    if number + n == 8
  ]
  result.sort(key=lambda r: r[1])
  return {'pairs': [r[0] for r in result]}

