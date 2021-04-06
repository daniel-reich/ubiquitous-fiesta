
def complete_square(a):
  height = len(a) 
  width = len(a[0])
  if height > width:
    for i in range((height - width)):
      for i in a:
        i.append(0)
  elif height == width:
    return a
  if height < width:
    for i in range((width - height)):
      a.append([0 for i in range(width)])
  return a

