
def digit_sort(lst):
  return sorted(lst,key = lambda n: (-len(str(n)),n))

