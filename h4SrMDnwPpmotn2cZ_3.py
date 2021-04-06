
def sum_of_cubes(nums):
  s = []
  if nums == []:
    return 0
  else:
    for i in nums:
      s.append(i ** 3)
    return sum(s)

