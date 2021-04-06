
def number_pairs(txt):
  lst = [int(i) for i in txt[2:].split()]
  return sum(lst.count(i)//2 for i in set(lst))

