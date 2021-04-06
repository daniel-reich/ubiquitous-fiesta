
def identify(*cube):
  m = len(cube)
  n = max(len(row) for row in cube)
  missing = sum(n-len(row) for row in cube)
  if missing:
    return "Missing " + str(missing)
  return "Full" if m==n else "Non-Full"

