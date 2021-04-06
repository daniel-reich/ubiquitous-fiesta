
def replace(txt, r):
  return ''.join('#' if r[0] <= i <= r[2] else i for i in txt)

