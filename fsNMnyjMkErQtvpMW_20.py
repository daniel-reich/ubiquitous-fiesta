
def holey_sort(lst):
  return sorted(lst,key=lambda x:sum([str(x).count('4'),str(x).count('6'),2*str(x).count('8'),str(x).count('9'),str(x).count('0')]))

