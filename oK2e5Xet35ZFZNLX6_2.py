
def neighboring(txt):
  return all(abs(ord(l1)-ord(l2))==1 for l1,l2 in zip(txt,txt[1:]))

