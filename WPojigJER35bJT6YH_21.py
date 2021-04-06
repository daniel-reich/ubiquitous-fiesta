
def reversed_binary_integer(num):
  b = str(bin(num)[2:])
  rev = b[-1::-1]
  return int(rev,2)

