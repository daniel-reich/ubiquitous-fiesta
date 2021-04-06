
def fruit_salad(fruits):
  start, tail = [f[:len(f) // 2] for f in fruits], [f[len(f) // 2:] for f in fruits]
  return ''.join(sorted(start+tail))

