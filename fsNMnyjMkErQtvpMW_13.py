
def holey_sort(lst):
  holes = [sum(1 if i in '4690' else 2 if i=='8' else 0 for i in str(j)) for j in lst]
  return sorted(lst, key=lambda x:holes[lst.index(x)])

