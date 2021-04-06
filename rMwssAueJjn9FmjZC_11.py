
def number_pairs(txt):
  mems = txt.split()[1:]
  return sum([mems.count(a)//2 for a in sorted(set(mems)) if mems.count(a)>1])

