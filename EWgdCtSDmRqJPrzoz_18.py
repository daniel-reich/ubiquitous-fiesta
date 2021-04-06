
def peel_layer_off(lst):
  x = lst
  del x[0]
  del x[-1]
  for i in x:
    del i[0]
    del i[-1]
  return x

