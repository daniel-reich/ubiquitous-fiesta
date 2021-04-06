
def peel_layer_off(lst):
  del lst[0]
  del lst[-1]
  for x in range(0, len(lst)):
    del lst[x][0]
    del lst[x][-1]
  return lst

