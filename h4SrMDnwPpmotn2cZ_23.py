
def sum_of_cubes(nums):
  l = []
  for x in nums:
    l.append(x**3)
  return sum(l)
print(sum_of_cubes([1, 5, 9]))
print(sum_of_cubes([3, 4, 5]))
print(sum_of_cubes([]))

