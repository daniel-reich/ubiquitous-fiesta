
def volume_of_box(sizes):
  x = 1
  for i in sizes:
    x *= sizes[i]
  return x

