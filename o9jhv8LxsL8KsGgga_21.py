
def bound_sort(lst, bounds):
  sort_sub = sorted(lst[bounds[0]: bounds[1] + 1])
  print ("".join(map(str, sort_sub)))
  mapstr = ''.join(map(str, sort_sub)) in ''.join(map(str, sorted(lst)))
  print(mapstr)
  return mapstr

