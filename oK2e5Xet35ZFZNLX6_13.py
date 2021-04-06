
def neighboring(txt):
  for i, j in zip(txt, txt[1:]):
    if abs(ord(i) - ord(j)) != 1:
      return False
  return True

