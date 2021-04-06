
def digit_sort(lst):
  return sorted(lst, key=lambda i: (-len(str(i)), i))

