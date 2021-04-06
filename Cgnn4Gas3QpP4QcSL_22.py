
def sum_digits_in_range(n):
  result = 0
  for i in range(n):
    result = 10 * result + 45 * int('1'+'0'*i)
  return result

