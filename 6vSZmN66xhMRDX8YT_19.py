
def advanced_sort(lst):
  unique = []
  sort = []
  for item in lst:
    section = []
    if item not in unique:
      for x in range(lst.count(item)):
        section.append(item)
      sort.append(section)
      unique.append(item)
  return sort

