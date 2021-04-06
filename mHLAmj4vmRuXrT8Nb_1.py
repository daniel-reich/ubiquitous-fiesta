
def consecutive_combo(lst1, lst2):
  lst = sorted(lst1+lst2)
  return all(lst[i]-lst[i-1]==1 for i in range(1,len(lst)))

