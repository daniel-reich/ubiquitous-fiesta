
def reversed_binary_integer(num):
  return int(bin(num)[::-1][:-2], 2)

