
def digit_sort(lst):
  return [int(x) for x in sorted(sorted([str(n) for n in lst]),key=len,reverse=True)]

