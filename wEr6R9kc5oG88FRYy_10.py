
def get_frame(w, h, ch):
  if w <= 2 or h <= 2:
    return "invalid"
  frame = []
  for i in range(h):
    newstr = ""
    for k in range(w):
      if (i > 0 and i < h-1) and (k > 0 and k < w-1):
        newstr += " "
      else:
        newstr += ch
    frame.append([newstr])
  return frame

