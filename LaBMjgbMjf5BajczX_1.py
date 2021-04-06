
def count_layers(rug):
  layers = list()
  count = 0
  for layer in rug:
    if layer not in layers:
      layers.append(layer)
​
  return len(layers)

