
def unique_styles(lst):
  unique = set()
  for i in lst:
    for j in i.split(','):
      unique.add(j)
  return len(unique)

