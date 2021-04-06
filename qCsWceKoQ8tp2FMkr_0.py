
def is_triangle(*sides):
  return all(s < sum(sides) - s for s in sides)

