
matrix_multiply = lambda m, n: 'invalid' if len(m[0]) != len(n) \
  else [[sum(x*y for x, y in zip(r, c)) for c in zip(*n)] for r in m]

