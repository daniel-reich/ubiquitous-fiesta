
def is_checkerboard(lst):
  return all(all(x*y == 0 for x, y in zip(lst[i][:-1], lst[i][1:])) for i in range(len(lst)))

