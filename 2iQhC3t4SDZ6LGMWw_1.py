
def on_rectangle_bounds(P):
  C = lambda i: [p[i] for p in P]
  return all([any([p[i] in [min(C(i)), max(C(i))] for i in [0,1]]) for p in P])

