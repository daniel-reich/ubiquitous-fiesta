
def hamming_code(message):
  return ''.join(j*3 for i in message for j in bin(ord(i))[2:].zfill(8))

