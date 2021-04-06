
def count_layers(rug, layers = 1):
  x = len(rug) // 2
  y = len(rug[x]) // 2 + 1
  for i in range(1, len(rug[x][:y])):
    if rug[x][i] == rug[x][-i]: continue
    else: layers += 1
  return layers

