
def in_box(lst):
  return any("*" in i[1:-1] for i in lst)

