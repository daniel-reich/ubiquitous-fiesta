
def rotate_transform(lst, num):
  w = len(lst[0])
  h = len(lst)
  
  if num < 0:
    num = abs(num) % 4
    for _ in range(num):
      rotated = [[0] * w for _ in range(h)]
      for y in range(h):
        for x in range(w):
          rotated[h - x - 1][y] = lst[y][x]
        print(rotated)
      lst = rotated
  else:
    num = num % 4
    for _ in range(num):
      rotated = [[0] * w for _ in range(h)]
      for y in range(h):
        for x in range(w):
          rotated[x][w - y - 1] = lst[y][x]
        print(rotated)
      lst = rotated
  return lst

