
def complete_square(lst):
  if all([len(lst)==len(lst[i]) for i in range(0, len(lst))]): return lst
  elif len(lst) > len(lst[0]):
    return [k+[0,]*(len(lst)-len(lst[0])) for k in lst]
  elif len(lst[0]) > len(lst):
    for k in range(len(lst[0])-len(lst)): lst += [[0,]*len(lst[0])]
    return lst

