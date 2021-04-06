
def square_digits(n):
  return int(''.join([str(int(b)**2) for b in str(n)]))

