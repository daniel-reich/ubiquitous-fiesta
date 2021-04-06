
def left_rotations(txt):
  result = []
  a = len(txt)
  for i in range(a):
    result.append(txt[i:]+txt[0:i])
  return result
  
def right_rotations(txt):
  result = []
  a = len(txt)
  for i in range(a):
    if i != 0:
      result.append(txt[(a-i)%a:]+txt[0:a-i])
    else:
      result.append(txt[(a-i)%a:])
  return result

