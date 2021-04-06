
def sum_digits_in_range(n):
  result=0
  for i in range (n):
    result+=(result) * 10 + 45*(10**(i)) - result
  return result

