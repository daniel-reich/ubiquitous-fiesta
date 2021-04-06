
def do_darts_solver(s, n, t, accD, accS):
  if n == 0 and t == 0:
    accS.add(tuple(accD))
  elif n > 0 and t > 0 and len(s):
    d = s.pop()
    do_darts_solver(list(s), n, t, accD, accS)
    do_darts_solver(list(s), n-1, t-d, accD+[d], accS)
    do_darts_solver(list(s)+[d], n-1, t-d, accD+[d], accS)
  return accS
​
def darts_solver(sections, darts, target):
  darts = do_darts_solver(sorted(sections, reverse=True), darts, target, [], set([]))
  return ['-'.join(str(x) for x in d) for d in sorted(darts)]

