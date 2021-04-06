
def possible_path(lst):
  paths = [
    {1, 2},
    {2, "H"},
    {4, "H"},
    {3, 4}
  ]
  
  return all({a, b} in paths for a, b in zip(lst, lst[1:]))

