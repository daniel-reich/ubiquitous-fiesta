
def count_layers(rug):
  count = 1
  for n in range(len(rug)//2):
    if rug[n] != rug[n+1]:
      count += 1
  return count

