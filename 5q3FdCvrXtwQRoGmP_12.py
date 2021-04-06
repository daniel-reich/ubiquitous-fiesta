
def count_towers(towers):
  return int(sum(1 for x in towers[-1] for y in x if y == '#')/2)

