
def number_pairs(txt):
  lst = txt.split()[1:]
  return sum(lst.count(i)//2 for i in set(lst))

