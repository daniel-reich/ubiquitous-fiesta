
def identify(*cube):
  max_width = len(max(cube, key=len))
  min_width = len(min(cube, key=len))
  height = len(cube)
  
  if max_width == min_width == height:
    return "Full"
  
  if max_width == min_width != height:
    return "Non-Full"
  
  missing = max_width * height - len(sum(cube, []))
  return "Missing {}".format(missing)

