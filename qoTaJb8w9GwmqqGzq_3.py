
def is_subset(lst1, lst2):
  return sorted(set(lst1 + lst2)) == sorted(lst2)

