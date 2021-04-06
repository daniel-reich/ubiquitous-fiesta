
def get_frame(w, h, ch):
  first = ""
  middle = ""
  if w <= 2 or h <= 2:
    return "invalid"
  
  for each in range(w):
    first += ch
    if each > 0 and each < w - 1:
      middle += " "
    else:
      middle += ch
  first = [first]
  middle = [middle]
  arr = []
  arr.append(first)
  for each in range(1, h - 1):
    arr.append(middle)
  arr.append(first)
  return arr

