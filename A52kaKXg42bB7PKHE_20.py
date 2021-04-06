
def num_then_char(lst):
  slst = []
  for i in lst:
    for j in i:
      slst.append(j)
  flst, j, slst = [], 0, sorted([a for a in slst if type(a) != str]) + sorted([b for b in slst if type(b) == str])
  while j != len(lst):
    i, f = 0, []
    while i != len(lst[j]): f.append(slst[i + sum(len(lst[x]) for x in range(j)) if j else i]); i += 1
    flst.append(f); j += 1
  return flst

