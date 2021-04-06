
def sort_authors(lst):
  return sorted(lst, key=lambda i:i.split(' ')[-1].lower())

