
def number_pairs(txt):
  t = txt.split()[1:]
  return sum(t.count(x)//2 for x in set(t))

