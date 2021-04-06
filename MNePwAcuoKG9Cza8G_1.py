
def build_staircase(height, block):
  arr = []
  for i in range(1, height+1):
    arr.append(list(block*i + '_'*(height - i)))
  return arr

