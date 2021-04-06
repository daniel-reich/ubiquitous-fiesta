
def where_is_waldo(lst):
  d = dict()
  for y in range(len(lst)):
    for x in range(len(lst[y])):
      d[lst[y][x]] = d.get(lst[y][x], []) + [[y+1, x+1]]
  for k, v in d.items():
    if len(v) == 1:
      return v[0]

