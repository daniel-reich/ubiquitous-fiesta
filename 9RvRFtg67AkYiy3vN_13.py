
def rotations(txt, sign):
  return [txt[i*sign:] + txt[:i*sign] for i in range(len(txt))]
​
def left_rotations(txt):
  return rotations(txt, 1)
​
def right_rotations(txt):
  return rotations(txt, -1)

