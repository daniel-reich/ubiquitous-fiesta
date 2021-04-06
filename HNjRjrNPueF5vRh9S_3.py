
def hamming_code(message):
  octo=[bin(ord(x))[2:].zfill(8) for x in message]
  A=[''.join([3*x for x in y]) for y in octo]
  return ''.join(A)

