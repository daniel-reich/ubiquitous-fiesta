
def holey_sort(lst):
  return sorted(lst, key=lambda x: sum(str(x).count(i) for i in '4690') + str(x).count('8')*2)

