
def left_rotations(txt):
  k = [txt]
  for i in txt[:-1]:
    j = txt[1:] + txt[0]
    txt = j
    k.append(j)
  return k
    
def right_rotations(txt):
  k = [txt]
  for i in txt[:-1]:
    j = txt[-1] + txt[:-1]
    txt = j
    k.append(j)
  return k

