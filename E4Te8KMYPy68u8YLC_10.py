
def volume_of_box(sizes):
  volume = 1
  for x in sizes.values():
    volume *= x
  return volume

