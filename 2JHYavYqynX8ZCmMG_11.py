
def ascii_sort(lst):
  return min(lst[0], lst[1], key=lambda w: sum(ord(c) for c in w))

