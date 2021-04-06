
def left_rotations(txt):
  return [txt[i:] + txt[:i] for i in range(len(txt))]
​
def right_rotations(txt):
  l = len(txt)
  return [txt[l-i:] + txt[:l-i] for i in range(len(txt))]

