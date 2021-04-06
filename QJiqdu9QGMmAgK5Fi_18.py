
def is_equal(obj_one, obj_two):
  for key, value in obj_one.items():
    if obj_one[key] != obj_two[key]:
      return False
      break
    else:
      return True

