
def consecutive_combo(lst1, lst2):
  return (sorted(lst1+lst2)) == [i for i in range(min(lst1+lst2), max(lst1+lst2)+1)]

