
def build_staircase(height, block):
  lst = [list((block * i) + ('_' * (height - i))) for i in range(1, height + 1)]
  return lst

