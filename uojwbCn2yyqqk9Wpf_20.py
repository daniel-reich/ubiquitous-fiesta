
import math
def aliquot_sum(n, max_n):
  sum = 1
  for i in range(2, n):
    if sum > max_n:
      return 0
    if n % i == 0:
      if i*i == n:
        return sum + i
      elif i*i > n:
        return sum
      else:
        sum += i + n // i
  return 1
        
def is_untouchable(number):
  if number < 2:
    return "Invalid Input"
  nums = []
  for i in range(2, number * number + 1):
    if i % 2 == 1 and number % 2 == 0 and math.sqrt(i) != int(math.sqrt(i)):
      continue
    asum = aliquot_sum(i, number)
    if asum == number:
      nums.append(i)
  if len(nums) == 0:
    return True
  return nums

