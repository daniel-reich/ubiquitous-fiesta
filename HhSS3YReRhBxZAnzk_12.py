
def gen_values(n, i):
  if isinstance(n, float) or isinstance(i, float):
    return [round(t*i,2) for t in range(int(n/i)+1)]
  return [t*i for t in range((n//i)+1)]

