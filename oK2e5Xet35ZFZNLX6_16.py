
def neighboring(txt):
  return all(ord(i) == ord(j) + 1 or ord(i) == ord(j) - 1 for i, j in zip(txt, txt[1:]))

