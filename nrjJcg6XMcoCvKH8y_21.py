
def validate_subsets(subsets, my_set):
  subs = [set(sub) for sub in subsets]
  my_set = set(my_set)
  return all(False for sub in subs if not sub.issubset(my_set) )

