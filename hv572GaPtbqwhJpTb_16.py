
def elasticize(w):
  m = (len(w) + 1) // 2 # midpoint
  l, r = w[:m], w[m:]   # left, right
  return ''.join([l[i]*(i+1) for i in range(len(l))] \
    + [r[-i]*i for i in range(len(r),0,-1)])

