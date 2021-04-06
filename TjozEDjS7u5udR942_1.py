
def sort_authors(lst):
  return sorted(lst, key=lambda x: x.lower().split()[-1])

