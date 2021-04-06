
def peel_layer_off(lst):
  return [[col for col in row[1:-1]] for row in lst[1:-1]]

