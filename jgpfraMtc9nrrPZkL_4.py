
def switch_gravity_on(lst):
  return [list(j) for j in zip(*(sorted(i) for i in zip(*lst)))][::-1]

