
d = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
def holey_sort(lst):
  y = [str(a) for a in lst]
  new = []
  for a in y:
    s = 0
    for b in a:
      if b in d:
        s += d[b]
    new.append([s,a])
  fin = []
  while new:
    fin.append(int([x[1] for x in new if x[0] == min([x[0] for x in new])][0]))
    new.pop([new.index(x) for x in new if x[0]==min((x[0] for x in new))][0])
  return fin

