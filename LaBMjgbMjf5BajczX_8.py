
import itertools as it
def count_layers(rug):
  mid_y = len(rug)        // 2
  mid_x = len(rug[mid_y]) // 2 + 1
  return len(list(it.groupby(rug[mid_y][:mid_x])))

