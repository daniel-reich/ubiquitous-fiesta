
def can_see_stage(seats):
  return all(all(x < y for x, y in zip(s, s[1:])) for s in zip(*seats))

