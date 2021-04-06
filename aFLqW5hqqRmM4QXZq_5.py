
def bar_chart(results):
  a = sorted([[k, v] for v, k in results.items()], reverse=True)
  rv = list(results.values())
  idx, qs = [], []
  for i, q in enumerate(a):
    if rv.count(q[0]) > 1:
      idx += [i]
      qs += [q]
  if len(idx) > 0:
    qs = sorted(qs)
    for i, x in zip(idx,qs):
      a[i] = x
  r = ""
  for q in a:
    r += q[1] + "|" + "#" * int(q[0]/50)
    if q[0] == 0: r+= str(q[0])
    else: r += " " +str(q[0])
    r += "\n"
  return r[:-1]

