
def my_sub(a, b):
  while a != 0:
    borrow = (~b) & a
    b = b ^ a
    a = borrow << 1
  return b

