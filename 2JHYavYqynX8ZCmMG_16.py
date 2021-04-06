
def ascii_sort(lst):
  return sorted(lst,key = lambda x: sum(ord(c) for c in x))[0]

