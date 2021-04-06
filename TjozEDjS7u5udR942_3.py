
def sort_authors(lst):
  def last_lower(x):
    return x.split()[-1].upper()
  return sorted(lst, key=last_lower)

