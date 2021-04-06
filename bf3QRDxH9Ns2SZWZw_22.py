
gn = lambda i, j, l, m, n: [i for i in ([(i+1, j), (i-1, j), (i, j+1), (i, j-1)] if n=='+' else [(i+1, j-1), (i-1, j+1), (i+1, j+1), (i-1, j-1)]) if 0<=i[0]<l and 0<=i[1]<m]
def all_explode(g, c = (0, 0), f=1):
  b = g[c[0]][c[1]]
  if str(b) in '+x':
    g[c[0]][c[1]] = 0
    [all_explode(g, i, 0) for i in gn(c[0], c[1], len(g), len(g[0]), b)]
  if f: return all(not any(str(j)!='0' for j in i) for i in g)

