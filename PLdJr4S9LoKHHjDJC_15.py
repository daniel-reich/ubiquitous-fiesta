
def identify(*cube):
  almost_full = all(len(cube[0])==len(cube[i]) for i in range(len(cube)))
  if almost_full and len(cube[0])==len(cube):
    return "Full"
  if almost_full:
    return "Non-Full"
  big = len(max(cube,key=len))
  return "Missing {}".format(sum(big-len(i) for i in cube))

