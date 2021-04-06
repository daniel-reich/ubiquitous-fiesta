
def replace(txt, r):
  return ''.join('#' if ord(i) in range(ord(r[0]), ord(r[2]) + 1) else i for i in txt)

