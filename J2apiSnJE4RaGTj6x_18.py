
def find_broken_keys(txt1, txt2):
  a = set()
  for c1, c2 in zip(txt1, txt2):
    if c1 != c2:
      a.add(c1)
  return sorted(list(a), key=txt1.find)

