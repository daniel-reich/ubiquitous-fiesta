
def digit_sort(lst):
  return list(map(int, sorted(map(str, sorted(lst)), key=len, reverse=True)))

