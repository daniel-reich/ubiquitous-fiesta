
def staircase(n):
  a = []
  d = abs(n)
  for i in range(1, d+1):
      a.append((d - i)*"_" + i * "#")
  return "\n".join(a) if n>0 else "\n".join(a[::-1])

