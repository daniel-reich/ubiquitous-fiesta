
def hamming_code(message):
  def hamming(x):
    return "".join(x*3 for x in "{:0>8}".format(bin(ord(x))[2:]))
  return "".join(map(hamming,message))

