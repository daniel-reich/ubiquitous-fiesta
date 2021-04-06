
def hamming_code(message):
  arr = list("{0:08b}".format(ord(x)) for x in list(message))
  return "".join(sum(list(list(a*3 for a in y) for y in [list(x) for x in arr]),[]))

