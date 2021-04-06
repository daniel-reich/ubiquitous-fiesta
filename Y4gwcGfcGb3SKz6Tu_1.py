
def max_separator(s):
  a = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)] 
  b = sorted([x for x in a if x[0] == x[-1] and len(x) >= 2])
  c = sorted([x for x in b if x[0] not in x[1:-1]],key=len)
  res = [x for x in c if len(x) == max(len(x) for x in c)]
  return [i[0] for i in res]

