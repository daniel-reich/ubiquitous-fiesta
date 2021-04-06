
def peel_layer_off(lst):
  return [[lst[x][y] for y in range(1, len(lst[x])-1)] for x in range(1, len(lst)-1)]

