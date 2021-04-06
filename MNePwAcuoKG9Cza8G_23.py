
def build_staircase(height, block):
  stairs=[]
  for i in range(1,height+1):
    c=[]
    for x in range(i):
      c.append(block)
    for x in range(height-i):
      (c.append('_'))
    stairs.append(c)
  return stairs

