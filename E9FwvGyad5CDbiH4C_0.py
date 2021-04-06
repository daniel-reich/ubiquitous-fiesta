
def block(lst):
  return sum(len(i) - i.index(2) - 1 for i in zip(*lst) if 2 in i)

