
def n_differences(lst):
  while len(lst)>1:
    lst=[lst[i]-lst[i-1] for i in range(1, len(lst))]
  return lst[0]

