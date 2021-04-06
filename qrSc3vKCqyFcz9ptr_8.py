
def sum_round(num):
  
  digits = [int(n) for n in reversed(str(num))]
  rounded = [str(digits[n] * (10 ** n)) for n in range(len(digits)) if digits[n] != 0]
  
  return ' '.join(rounded)

