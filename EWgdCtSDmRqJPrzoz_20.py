
def peel_layer_off(lst):
  a = [i[1:-1] for i in lst]
  a.pop()
  return a[1:]

