
def route_diff(d):
  return len(d) - abs(d.count("N") - d.count("S")) - abs(d.count("E") - d.count("W"))

