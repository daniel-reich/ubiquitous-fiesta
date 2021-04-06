
def number_of_days(coordinate):
  s = sum(x if x >=0 else -x for x in coordinate)
  return s + s//5 if s % 5 else s + s//5 -1

