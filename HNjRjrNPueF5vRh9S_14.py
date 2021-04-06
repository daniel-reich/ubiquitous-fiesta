
def hamming_code(message):
  l = ["{:08b}".format(ord(i)) for i in list(message)]
  h = [i*3 for j in l for i in j]
  return ''.join(h)

