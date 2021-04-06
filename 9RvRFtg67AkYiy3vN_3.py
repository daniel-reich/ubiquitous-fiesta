
def left_rotations(txt):
  count = 1
  rotated_lst = []
  rotated_lst.append(txt)
  while count < len(txt):
    txt = txt[1:] + txt[0]
    rotated_lst.append(txt)
    count += 1
  return rotated_lst
​
def right_rotations(txt):
  count = 1
  rotated_lst = []
  rotated_lst.append(txt)
  while count < len(txt):
    txt = txt[-1] + txt[:-1]
    rotated_lst.append(txt)
    count += 1
  return rotated_lst

