
def split(number):
  if number < 3: return number
  a = number%3
  b = number//3
  if a <= 1:
      return 3 ** (b-1) * (a+3)
  else:
      return 3**b * a

