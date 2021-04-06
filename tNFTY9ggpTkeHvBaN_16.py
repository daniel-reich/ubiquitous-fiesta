
def total_volume(*boxes):
  result = 0
  for box in boxes:
    result = result + volume(box)
  return result
​
def volume(box):
  l = box[0]
  w = box[1]
  h = box[2]
  return l*w*h

