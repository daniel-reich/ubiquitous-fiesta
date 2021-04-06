
def left_rotations(txt):
  output = [txt]
  rotstring = txt[1:]+txt[0]
  output.append(rotstring)
  while rotstring != txt:
    rotstring = rotstring[1:]+rotstring[0]
    output.append(rotstring)
  return output[:-1]
​
def right_rotations(txt):
  output = [txt]
  rotstring = txt[-1]+txt[:-1]
  output.append(rotstring)
  while rotstring != txt:
    rotstring = rotstring[-1]+rotstring[:-1]
    output.append(rotstring)
  return output[:-1]

