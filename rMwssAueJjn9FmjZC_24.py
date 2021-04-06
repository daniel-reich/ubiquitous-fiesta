
def number_pairs(txt):
  txt = txt.split()[1:]
  return sum(txt.count(n)//2 for n in set(txt) if txt.count(n)>1)

