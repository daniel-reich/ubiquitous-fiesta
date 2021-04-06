
def prime_numbers(num):
  if num < 0:
    return 0
  count = 1
  numbers = [i for i in range(3,num+1)]
  for nums in numbers:
    if len([i for i in range(2, nums) if nums % i == 0]) == 0:
      count += 1
  else:
    return count

