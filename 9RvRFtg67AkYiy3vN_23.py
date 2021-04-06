
def left_rotations(txt):
  return [txt[x:]+txt[:x] for x in range(0,len(txt))]
​
def right_rotations(txt):
  return [txt[x:]+txt[:x] for x in range(len(txt),0,-1)]

