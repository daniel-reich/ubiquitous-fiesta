
def min_difference_pair(nums):
  minPair = [sorted(nums)[0], sorted(nums)[1]]
  for i in range(1, len(nums) - 1):
    num1, num2 = sorted(nums)[i], sorted(nums)[i + 1]
    if (num2 - num1) < (minPair[1] - minPair[0]):
      minPair = [num1, num2]
  return minPair

