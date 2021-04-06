
def is_center(rug):
  flat_rug = ''.join(rug)
  return len(set([piece for piece in flat_rug])) == 1
def remove_layer(rug):
  layer_pattern = rug[0][0]
  while rug[0][0] == layer_pattern:
    if len([pattern for pattern in rug[0] if pattern != layer_pattern]) == 0:
      rug = rug[1:len(rug) - 1]
    for i in range(len(rug)):
      rug[i] = rug[i][1:len(rug[i])-1]
  return rug
def count_layers(rug):
  if is_center(rug):
    return 1
  rug = remove_layer(rug)
  return 1 + count_layers(rug)

