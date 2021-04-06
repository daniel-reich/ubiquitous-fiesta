
def build_staircase(height, block):
  return [[block] * foo + ["_"] * (height - foo) for foo in range(1, height + 1)]

