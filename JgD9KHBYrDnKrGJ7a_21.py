
def swap_dict(dic):
  D = {v:[] for v in dic.values()}
  for k, v in dic.items():
    D[v].append(k)
  return D

