
def staircase(n):
  res = []
  for k in range(1, abs(n)+1):
    res.append(("_"*(abs(n)-k)) + ("#"*k))
  return "\n".join(res) if n > 0 else "\n".join(res[::-1])

