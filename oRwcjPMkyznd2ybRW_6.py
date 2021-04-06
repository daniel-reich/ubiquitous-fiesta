
def max_product(n):
  def p(k):
    c=1
    for i in str(k):c*=int(i)
    return c
  d={}
  for i in range(n+1):
    if p(i) not in d:d[p(i)]=[i]
    else: d[p(i)].append(i)
  return d[max(d)]

