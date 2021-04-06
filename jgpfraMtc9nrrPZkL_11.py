
def switch_gravity_on(lst):
  return [list(i) for i in zip(*[sorted(i,key=lambda x:x!='-') for i in zip(*lst)])]

