
def is_rectangle(coordinates):
  if len(coordinates) != 4:
    return False
  for item in coordinates:
    if coordinates.count(item) > 1:
      return False
  array = []
  for item in coordinates:
    array.append([((item.split(",")[0])[1:]).strip(), ((item.split(",")[1])[:-1]).strip()])
  Xs = []
  Ys = []
  for item in array:
    Xs.append(item[0])
    Ys.append(item[1])
  return len(set(Xs)) == 2 and len(set(Ys)) == 2

