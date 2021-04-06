
def count_layers(rug):
  return sum(a != b for a, b in zip(rug[len(rug) // 2], rug[len(rug) // 2][1:])) / 2 + 1

