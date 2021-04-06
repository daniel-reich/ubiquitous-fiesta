
def reversed_binary_integer(num):
  return int((str(bin(num))[2::])[::-1],2)

