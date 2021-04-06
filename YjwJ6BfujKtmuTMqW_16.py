
def dice_game(s):
  p = [1, 2, 3, 4]
  while len(p) > 1:
    p = {k: s.pop(0) for k in p}
    q = sorted(p, key=lambda x: [sum(p[x]), p[x][0]])
    if all(p[q[0]] != p[k] for k in q[1:]): p = sorted(q[1:])
  return 'p{}'.format(p[0])

