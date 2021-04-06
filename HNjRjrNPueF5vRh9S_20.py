
def hamming_code(message):
  return "".join("".join(b * 3 for b in "{:08b}".format(ord(c))) for c in message)

