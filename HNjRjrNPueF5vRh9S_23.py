
def hamming_code(message):
  bits = [bin(ord(i))[2:].zfill(8) for i in message]
  return ''.join(i*3 for bit in bits for i in bit)

