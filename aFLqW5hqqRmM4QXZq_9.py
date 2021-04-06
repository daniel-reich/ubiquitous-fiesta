
def bar_chart(results):
  tups = list(results.items())
  tups  = sorted(tups, key = lambda x: (-x[1],x[0]))
  return '\n'.join([q[0]+"|"+"#"*(q[1]//50)+(" " if q[1] > 0 else "")+str(q[1])
  for q in tups])

