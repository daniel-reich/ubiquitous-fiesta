
def sum_digits_in_range(n):
  if n==0: return 0
  return 45*10**(n-1) + 10*SumDigitsInRange(n-1)

