
def product(lst):
  meh = sorted(set(lst))
  return meh[-1]*meh[-2] if len(meh)>1 else meh[-1]**2

