
def identify(*cube):
  n = len(cube)
  max1 = 1
  for i in range(n):
    max1 = max(max1, len(cube[i]))
  total = 0
  for i in range(n):
    total += max1 - len(cube[i])
  return 'Missing {}'.format(total) if total else 'Non-Full' if max1 > len(cube) else 'Full'

