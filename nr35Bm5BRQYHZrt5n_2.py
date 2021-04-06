
def upward_trend(lst):
  return all([lst[i] < lst[i+1] for i in range(len(lst) - 1)]) if all([isinstance(i,int) for i in lst]) else "Strings not permitted!"

