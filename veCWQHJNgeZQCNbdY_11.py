
def root_digit(n):
  sum_digits = 0
  for i in str(n):
    sum_digits += int(i)
  if sum_digits > 9:
    return root_digit(sum_digits)
  return sum_digits

