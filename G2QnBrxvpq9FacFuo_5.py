
def possible_path(lst):
  if len(lst) == 1:
    return True
  return all(idx % 2 for idx, i in enumerate(lst) if i == "H") or \
    all(not idx % 2 for idx, i in enumerate(lst) if i == "H") and not lst.count("H") % 2

