
def reverse_title(txt):
  l = [x for x in txt.split()]
  m = []
  for i in l:
    m.append(i[0].lower() + i[1:].upper())
  m = " ".join(m)
  return m

