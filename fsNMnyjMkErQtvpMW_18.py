
def holey_sort(lst):
  holes = {'1': 0, '2': 0, '3': 0, '4': 1, '5': 0,
  '6': 1, '7': 0, '8': 2, '9': 1, '0': 1}
  return sorted(lst, key=lambda i: sum(holes[j] for j in str(i)))

