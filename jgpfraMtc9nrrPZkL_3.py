
def switch_gravity_on(lst):
  return [list(z) for z in zip(*[sorted(l)[::-1] for l in zip(*lst)])]

