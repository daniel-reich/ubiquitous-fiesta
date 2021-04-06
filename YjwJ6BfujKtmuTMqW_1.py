
def dice_game(scores):
  p = ["p1", "p2", "p3", "p4"]
  r = iter((sum(x), x[0]) for x in scores)
  while len(p) > 1:
    s = sorted(zip(p,r),key=lambda x: x[1])
    if s[0][1] == s[1][1]:
      continue
    p.remove(s[0][0])
  return p[0]

