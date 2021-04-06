
def possible_path(lst):
  d = {1: (2,), 2: (1,"H"), "H" : (2,4), 4:('H',3), 3:(4,)}
  return all(lst[x+1] in d[lst[x]] for x in range(len(lst)-1))

