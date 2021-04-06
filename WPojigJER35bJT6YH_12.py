
def reversed_binary_integer(num):
  return int('0b'+bin(num)[2:][::-1], 2)

