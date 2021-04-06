
def simple_comp(lst1, lst2):
  try:
    return sorted(map(lambda x: x * x, lst1)) == sorted(lst2)
  except TypeError:
    return False

