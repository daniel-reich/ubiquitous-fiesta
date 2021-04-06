
def coord_str(x, y):
  return str(x) + "_" + str(y)
​
def is_exitable(lst, x, y, visited, exit, max_x, max_y):
  if x < 0 or y < 0 or x > max_x or y > max_y or lst[y][x] == 1:
    return False
  current = coord_str(x, y)
  if current in visited:
    return False
  visited.add(current)
  #print(current)
​
  found_exit = (current == exit or
    is_exitable(lst, x+1, y, visited, exit, max_x, max_y) or
    is_exitable(lst, x, y+1, visited, exit, max_x, max_y) or
    is_exitable(lst, x-1, y, visited, exit, max_x, max_y) or
    is_exitable(lst, x, y-1, visited, exit, max_x, max_y))
​
  visited.remove(current)
  return found_exit
​
def can_exit(lst):
  max_x = len(lst[0]) - 1
  max_y = len(lst) - 1
  exit = coord_str(max_x, max_y)
  return is_exitable(lst, 0, 0, set(), exit, max_x, max_y)
​
​
print("0_0" in {"0_0"})
​
print(can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
])) # true
​
print(can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
])) # false
​
# This maze only has dead ends!
​
print(can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1]
])) # false
​
# Exit only one block away, but unreachable!
​
print(can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 0]
])) # true

