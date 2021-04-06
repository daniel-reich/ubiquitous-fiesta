
def spin_around(lst):
  return abs(sum(90 if i == "right" else -90 for i in lst))//360

