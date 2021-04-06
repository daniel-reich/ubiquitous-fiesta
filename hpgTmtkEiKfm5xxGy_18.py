
def distance(x, y):
  return (x**2 + y**2)**0.5
​
def paths(x, y):
  def find_paths(x, y, path):
    if x == 0 and y == 0:
      paths.add(path)
      return
    directions = [
      (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    cur_distance = distance(x, y)
    for change_x, change_y in directions:
      new_x = x + change_x
      new_y = y + change_y
      if distance(new_x, new_y) <= cur_distance:
        find_paths(new_x, new_y, ','.join((path, str((new_x, new_y)))))
  paths = set()
  find_paths(x, y, '')
  return len(paths)

