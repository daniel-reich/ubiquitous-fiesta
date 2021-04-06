
def wiggle_string(s):
  return [" " * (len(s) - abs(i)) + s for i in range(-len(s), len(s) + 1)]

