
def peel_layer_off(lst):
  return [[lst[i][j] for j in range(1,len(lst[i])-1)] for i in range(1,len(lst)-1)]

