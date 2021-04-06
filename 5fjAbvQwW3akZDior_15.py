
def unrepeated(txt):
  lst = []
  for l in txt:
    if l not in lst:
      lst.append(l)
  return "".join(lst)

