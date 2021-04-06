
def sort_authors(lst):
  return sorted( lst, key = lambda s: s.split()[-1].lower() )

