
def sum_digits(a, b):
  sum = 0
  for i in range(a,b+1):
    for j in str(i):
      sum += int(j)
  return sum

