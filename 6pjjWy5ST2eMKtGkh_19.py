
def replace(txt, r):
  rng = [chr(i) for i in range(ord(r[0]), ord(r[-1])+1)]
  return ''.join(i if i not in rng else '#' for i in txt)

