
def sort_authors(lst):
  return sorted(lst,key=lambda x: x.split()[-1][0].lower())

