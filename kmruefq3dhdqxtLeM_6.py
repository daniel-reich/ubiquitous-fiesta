
def sum_digits(a, b):
  ov_total = 0
  for x in range(a, b+1):
    total = 0
    for digit in str(x):
      total += int(digit)
    ov_total += total
  return ov_total

