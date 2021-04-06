
def bridge_shuffle(lst1, lst2):
  return sum([[lst1.pop(0), lst2.pop(0)] for i in range(min(len(lst1), len(lst2)))],[])+lst1+lst2

