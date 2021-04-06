
def swap_d(k, v, swap):
  if swap:
    return {m:n for n,m in zip(k,v)}
  else: return {n:m for n,m in zip(k,v)}

