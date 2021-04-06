
def clean_up(files, sort):
  f = {"prefix": lambda t: t[:t.rindex(".")], "suffix": lambda t: t[t.rindex("."):]}
  d = {}
  q = []
  for i in files:
    x = f[sort](i)
    if x not in q:
      q.append(x)
      d[x] = []
    d[x].append(i)
  return [d[i] for i in q]

