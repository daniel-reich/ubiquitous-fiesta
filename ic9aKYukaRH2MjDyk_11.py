
def sort_by_last(txt):
  lst = txt.split()
  map = {}
  for str in lst:
    key = getUniqueKey(str[-1], map)
    map[key] = str
  strsorted  = ""
  for key in sorted(map):
    strsorted += " " + map[key]
  return strsorted[1:]
​
def getUniqueKey(str, map):
  if str in map:
    return getUniqueKey(str+str, map)
  else:
    return str

