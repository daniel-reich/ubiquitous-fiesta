
def sort_authors(lst):
  lst.sort(key = lambda v: ((v.split(' '))[-1]).upper())
  print(lst)
  return lst

