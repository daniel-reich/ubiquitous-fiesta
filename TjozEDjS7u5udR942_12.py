
def sort_authors(lst):
  return sorted(lst, key = lambda x: x[x.rfind(" ") + 1:].upper())

