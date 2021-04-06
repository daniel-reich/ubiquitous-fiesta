
def solve_for_exp(a, b):
  count = 0
  while True:
    if a ** count == b:
      break
    else:
      count += 1
​
  return count

