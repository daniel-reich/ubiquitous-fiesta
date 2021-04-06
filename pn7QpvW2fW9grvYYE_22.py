
def find_fulcrum(lst):
  for i in range(len(lst)):
    A = sum([lst[j] for j in range(i)])
    B = sum([lst[k] for k in range(i + 1, len(lst))])
    if A == B: return lst[i]
  return -1

