
def num_of_digits(num):
  digs = 0
  while abs(num) >= 1:
    num /= 10
    digs += 1
  return digs if digs > 1 else 1

