
def reverse_complement(inp):
  return ''.join("UACG"["AUGC".index(i)] for i in inp)[::-1]

