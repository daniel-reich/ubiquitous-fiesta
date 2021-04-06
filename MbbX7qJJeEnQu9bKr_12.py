
def max_occur(txt):
  dct = {}
  for i in set(txt):
    dct[i] = txt.count(i)
  mx = max(dct.values())
  return "No Repetition" if mx == 1 else \
      [i[0] for i in dct.items() if i[1] == mx]

