
def most_frequent_char(lst):
  txt = ''.join(lst)
  dct = {}
  for x in set(txt):
    c = txt.count(x)
    if c not in dct:
      dct[c] = [x]
    else:
      dct[c].append(x)
​
  return sorted(max(dct.items(), key = lambda x: x[0])[-1])

