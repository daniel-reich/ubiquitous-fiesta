
def square_digits(n):
  s = str(n)
  ar = [str(int(d)**2) for d in s]
  s = ''.join(ar)
  return int(s)

