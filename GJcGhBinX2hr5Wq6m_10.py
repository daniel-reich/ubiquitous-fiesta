
def move_zeros(lst):
  meh = [x for x in lst if type(x) not in [int,float] or x]
  return meh + [0]*(len(lst)-len(meh))

