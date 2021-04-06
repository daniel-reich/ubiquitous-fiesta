
def add(n1, n2):
  lon = [n1, n2]
  if '' in lon or None in lon:
    return "Invalid Operation"
  return str(int(n1) + int(n2))

