
def get_path_length(world, width, length):
  world = world.split(",")
  matt = [world.index("m")%width,world.index("m")//width]
  house = [world.index("h")%width,world.index("h")//width]
  world = [world[i:i+width] for i in range(0, len(world), width)]
​
  def get_neighbors(x, y):
    return [[x+xi, y+yi] for xi in [-1,0,1] for yi in [-1,0,1] if x+xi in range(width) and y+yi in range(length) and [x+xi, y+yi] not in seen and [x+xi, y+yi] not in current and [x+xi, y+yi] not in nxt and world[y+yi][x+xi] != "t"]
​
  current = [matt]
  seen = []
  nxt = []
  i = 0
  while current:
    if house in current: return i
    for c in current:
      nxt += get_neighbors(*c)
    seen += current
    current = nxt
    nxt = []
    i += 1
  return -1

