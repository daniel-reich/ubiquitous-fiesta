
def reversed_binary_integer(num):
  return int(bin(num)[:2] + bin(num)[2:][::-1], 2)

