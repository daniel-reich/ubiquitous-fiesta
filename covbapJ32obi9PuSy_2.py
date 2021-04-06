
def diamond_arrays(x):
  length = range(1, x + 1)
  lst = [[number] * number for number in length]
  reverse = lst[:-1][::-1]
  return lst + reverse

