
def hamming_code(message):
  return ''.join(bit*3 for ch in message for bit in format(ord(ch), '08b'))

