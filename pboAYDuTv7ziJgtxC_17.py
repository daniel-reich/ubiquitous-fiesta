
def min_turns(current, target):
  d=0
  for i in range(4):
    if abs(int(current[i])-int(target[i]))>5 :
      d+=10-abs(int(current[i])-int(target[i]))
    else:
      d+=abs(int(current[i])-int(target[i]))
  return d

