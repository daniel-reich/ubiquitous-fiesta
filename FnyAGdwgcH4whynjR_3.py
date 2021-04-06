
import itertools
def get_subsets(lst, n):
  lsts = []
  for L in range(0, len(lst)+1):
    for subset in itertools.combinations(lst, L):
      if sum(list(subset)) == n:
        lsts.append(list(subset))
  for i in range(len(lsts)):
    for x in range(i, len(lsts)):
      if len(lsts[i]) > len(lsts[x]):
        lsts[i], lsts[x] = lsts[x], lsts[i]
  for i in range(len(lsts)):
    for x in range(i, len(lsts)):
      if len(lsts[i]) == len(lsts[x]):
        for a in range(len(lsts[i])):
          if lsts[i][a] != lsts[x][a]:
            if lsts[i][a] > lsts[x][a]:
              lsts[i], lsts[x] = lsts[x], lsts[i]
            break
  for i in lsts:
    print(i)
  return lsts

