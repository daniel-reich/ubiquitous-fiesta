
def left_rotations(txt):
  return [txt[i:]+txt[:i] for i in range(len(txt))]
​
def right_rotations(txt):
  return [txt]+[txt[i:]+txt[:i] for i in range(len(txt))][1:][::-1]

