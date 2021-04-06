
def build_staircase(height, block):
  op = []
  for i in range(1, height+1):
    s = block*i + "_"*(height-i)
    op.append(list(s))
  return op

