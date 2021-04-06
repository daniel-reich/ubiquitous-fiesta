
def rotate(mat: list):
  return list(map(list, map(reversed, zip(*mat))))

