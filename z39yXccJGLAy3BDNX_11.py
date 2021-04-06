
def flipping_bits(n):
  return int("".join(str(int(not int(x))) for x in "{:0>32}".format(bin(n)[2:])),2)

