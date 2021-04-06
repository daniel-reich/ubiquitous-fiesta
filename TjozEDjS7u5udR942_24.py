
def sort_authors(lst):
  return sorted(lst, key=lambda v: v.split()[-1].lower())

