
def left_rotations(txt):
  left_lst = []
  i = 0
  while i < len(txt):
    new_txt = txt[i:] + txt[:i]
    left_lst.append(new_txt)
    i += 1
  return left_lst
​
def right_rotations(txt):
  right_lst = []
  i = 0
  while i < len(txt):
    new_txt = txt[-i:] + txt[:-i]
    right_lst.append(new_txt)
    i += 1
  return right_lst

