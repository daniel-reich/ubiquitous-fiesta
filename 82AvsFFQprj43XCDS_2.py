
def no_strangers(txt):
  txt = txt.split()
  d, k3, k5 = {}, [], []
  for w in txt:
    w = w.lower().rstrip('.,:;!?"\'').lstrip('"\'')
    k = d.get(w, 0) + 1
    d[w] = k
    if k == 3: k3.append(w)
    if k == 5: k5.append(w); k3.remove(w)
  return [k3, k5]

