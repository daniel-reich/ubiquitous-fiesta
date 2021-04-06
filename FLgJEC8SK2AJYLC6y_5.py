
def possible_path(lst):
  d={1:[2],2:[1,'H'],3:[4],4:[3,'H'],'H':[2,4]}
  return all(x[1] in d[x[0]] for x in zip(lst,lst[1:]))

