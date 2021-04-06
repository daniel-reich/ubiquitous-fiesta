
def max_collatz(num):
  results = [num]
  while num != 1:
    if num % 2:
      num = (num * 3) + 1
    else:
      num /= 2 
    results.append(num)
  return max(results)

