
def greater_permutation(exp, n):
  v = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
  v = [exp.replace('a', str(n[x[0]])).replace('b', str(n[x[1]])).replace('c', str(n[x[2]])) for x in v]
  d, i = [eval(x) for x in v[:]], -10
  i = d.index(max(d))
  return ['{} = {:0.0f}', '{} = {:0.2f}'][bool(d[i] % 1)].format(v[i], d[i])

