
def number_pairs(txt):
  lst = list(map(int,txt.split(' ')))[1:]
  C = [lst.count(i) for i in set(lst)]
  return sum(x//2 for x in C)

