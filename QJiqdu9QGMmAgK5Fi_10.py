
def is_equal(obj_one, obj_two):
  return all(a==b for a, b in zip(obj_one.values(), obj_two.values()))

