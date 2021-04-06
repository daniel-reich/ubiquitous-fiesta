
def sum_digits(a, b):
  sum_dig = 0
  for i in range(a, b+1):
    for item in str(i):
      sum_dig += int(item)
  return sum_dig

