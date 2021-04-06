
def rotate_transform(lst, num):
  for _ in range(abs(num)):
    if num > 0:
      lst = list(map(list, zip(*lst[::-1])))
    else:
      lst = list(map(list, zip(*lst)))[::-1]
  return lst

