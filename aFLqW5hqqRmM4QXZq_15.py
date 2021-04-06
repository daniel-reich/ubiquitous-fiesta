
def bar_chart(results):
  res = []
  for r in results:
    n = '#'*(results[r]//50) + ' ' if results[r] > 0 else ''
    res.append('{}|{}{}'.format(r,n,results[r]))
  res.sort(key=lambda x: x[1])
  res.sort(key=lambda x: x.count('#'),reverse=True)
  return '\n'.join(res)

