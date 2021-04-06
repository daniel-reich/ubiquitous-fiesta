
def junction_or_self(n):
  out = []
  for i in range(n-1, 0, -1):
    if sum([int(d) for d in str(i)])+i == n:
      out.append(i)
  if len(out) == 0:
    return 'Self'
  else:
    return out

