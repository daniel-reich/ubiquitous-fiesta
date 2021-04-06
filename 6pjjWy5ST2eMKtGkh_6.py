
def replace(txt, r):
  return ''.join(['#' if ord(letter) in range(ord(r[0]), ord(r[-1]) + 1) else letter for letter in txt])

