
def ascending(txt):
  for n in range(1, len(txt)//2 + 1):
    groups = [txt[i:i+n] for i in range(0, len(txt), n)]
    if all(int(a) + 1 == int(b) for a, b in zip(groups, groups[1:])):
      return True
  return False

