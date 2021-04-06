
def split_into_buckets(p, n):
  p = p.split(" ")
  f = []
  for i in range(len(p)):
    if i != len(p) - 1 and len(p[i]) + 1 + len(p[i+1]) <= n:
      p[i+1] = p[i] + " " + p[i+1]
    elif len(p[i]) <= n:
      f.append(p[i])
    else:
      return []
  return f

