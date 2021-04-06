
def count_layers(rug):
  list = []
  ans = 0
  if len(rug) == 1:
    return 1
  for layer in rug:
    if layer not in list:
      ans += 1
      list.append(layer)
  return ans

