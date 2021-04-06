
def is_equal(obj_one, obj_two):
  for i in obj_one.keys():
    if i not in obj_two or obj_one[i]!=obj_two[i]:
      return False
  return True

