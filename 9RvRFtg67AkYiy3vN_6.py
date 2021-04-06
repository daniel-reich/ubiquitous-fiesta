
def left_rotations(txt):
  return [txt[n:] + txt[:n] for n in range(len(txt))] 
​
def right_rotations(txt):
  return [txt[len(txt)-n:] + txt[:len(txt)-n] for n in range(len(txt))]

