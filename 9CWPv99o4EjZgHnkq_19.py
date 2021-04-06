
def divide(lst, n):
  out = []
  total, chunk = 0, []
  for v in lst:
    if total + v <= n:
      chunk.append(v)
      total += v
    else:
      out.append(chunk)
      total, chunk = v, [v]
  if chunk:
    out.append(chunk)
  return out

