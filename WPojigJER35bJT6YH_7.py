
def reversed_binary_integer(num):
  binar = bin(num)
  reverse_binar = binar[2:][::-1]
  return int(reverse_binar,2)

