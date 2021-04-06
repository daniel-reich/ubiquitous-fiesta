
holes = lambda x: sum([ 2 if d == '8' else 1 if d in '4690' else 0 for d in str(x) ])
​
def holey_sort(l):
  return [ e[-1] for e in sorted([(holes(n), n) for n in l],key= lambda x: x[0]) ]

