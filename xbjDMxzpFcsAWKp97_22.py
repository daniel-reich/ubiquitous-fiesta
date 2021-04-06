
def can_see_stage(seats):
  seats_T = [list(item) for item in zip(*seats)]
  return len(list(filter(lambda x: sorted(x) == x and len(set(x)) == len(x), seats_T))) == len(seats_T)

