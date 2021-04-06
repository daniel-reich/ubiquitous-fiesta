
def neighboring(txt):
  return all(abs(ord(x) - ord(y)) == 1 and abs(ord(z) - ord(y)) == 1  \
    for x,y,z in zip(txt, txt[1:], txt[2:]))

