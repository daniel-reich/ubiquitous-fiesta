
def max_collatz(num):
  if num == 1:
    return 1
​
  else:
    collatz_nums = []
    while num != 1:
      collatz_nums.append(num)
      if num % 2 == 0:
        num /= 2
      else:
        num = num * 3 + 1
        
  return max(collatz_nums)

