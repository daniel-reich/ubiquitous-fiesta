
def one_odd_one_even(n):
  b = str(n)
  return int(b[0]) % 2 == 0 and int(b[1]) % 2 == 1 or int(b[0]) % 2 == 1 and int(b[1]) % 2 == 0

