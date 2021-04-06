
def move_zeros(lst):
  return [i for i in lst if type(i) == bool or i != 0] + [0] * min(lst.count(0), str(lst).count("0"))

