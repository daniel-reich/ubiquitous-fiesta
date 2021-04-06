
def bar_chart(results):
  quarters = sorted([(-v, k) for k,v in results.items()])
  return '\n'.join([k + '|' + '#'*(-v//50) + (' ' if v != 0 else '') + str(-v) for v,k in quarters])

