
def harmonic(n):
  try:
      a = [i for i in range(1, n+1)]
      b = [1 / i for i in a]
      return round(sum(b), 3) if n > -1 else 'none'
  except TypeError:
      print('Invalid Input, must be whole number')

