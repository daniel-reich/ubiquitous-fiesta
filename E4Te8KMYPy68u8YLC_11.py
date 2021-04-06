
def volume_of_box(sizes):
  result = 1
  for key in sizes:
    result = result * sizes[key]
  return result

