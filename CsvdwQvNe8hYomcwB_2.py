
def remap(v, l1, h1, l2, h2):
  return l2 + ((h2 - l2) / (h1 - l1)) * (v - l1) if (h1 - l1) != 0 else 0

