
def reversed_binary_integer(num):
  num = bin(num)
  return eval(num[:2]+num[::-1][:-2])

