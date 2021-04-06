
def one_odd_one_even(n):
  o = len([i for i in str(n) if int(i) % 2 != 0])
  e = len([i for i in str(n) if int(i) % 2 == 0])
  return o == e

