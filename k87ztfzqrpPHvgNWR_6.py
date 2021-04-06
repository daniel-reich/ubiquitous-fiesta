
def widen_streets(lst, n):
  gaps = [i for i in range(len(lst[0])) if lst[-1][i] == " "]
  return ["".join(" " * n if i in gaps else r[i] for i in range(len(r))) for r in lst]

