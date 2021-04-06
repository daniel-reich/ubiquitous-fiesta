
def spin_around(lst):
  return abs(90* lst.count("right") - 90 * lst.count("left"))//360

