
def reversed_binary_integer(num):
  return int("{0:0b}".format(num)[::-1], 2)

