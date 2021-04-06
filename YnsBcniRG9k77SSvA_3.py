
def print_all_groups():
  grp = ["a", "b", "c", "d", "e"]
  num = ["1", "2", "3", "4", "5", "6"]
  return ", ".join([i+x for i in num for x in grp])

