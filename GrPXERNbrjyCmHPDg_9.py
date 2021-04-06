
def duplicate_count(txt):
  saver = []
  savey = []
  counter = 0
  for i in txt:
    if (i not in saver) and (i not in savey):
      saver.append(i)
    elif i not in savey:
      savey.append(i)
      counter += 1
    else:
      pass
  return counter

