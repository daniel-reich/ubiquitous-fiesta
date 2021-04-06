
def holey_sort(lst):
  holes = {0:1, 4:1, 6:1, 8:2, 9:1}
  return sorted(lst, key=lambda x: sum(holes.get(int(i), 0) for i in str(x)))

