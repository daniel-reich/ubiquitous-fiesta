
def get_frame(w, h, ch):
  lst = []
  if w <= 2 or h <= 2:
    return "invalid"
  else:
    for i in range(h):
      temp = []
      if i == 0 or i == (h-1):
        temp.append(ch*w)
        lst.append(temp)
      else:
        temp.append(ch + ' '*(w-2) + ch)
        lst.append(temp)
    return lst

