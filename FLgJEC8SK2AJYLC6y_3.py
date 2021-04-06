
def possible_path(lst):
  valid = ["12", "2H", "H4", "43", "21", "H2", "4H", "34"]
  return all(str(a) + str(b) in valid for a, b in zip(lst, lst[1:]))

