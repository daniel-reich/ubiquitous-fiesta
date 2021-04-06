
def get_frame(w, h, ch):
  lst = []
  x = w-2
  if w<3 or h<3:
    return "invalid"
  else :
    for i in range(h):
      if i in (0,h-1):
        lst.append ([ch*w])
      else:
        lst.append ([ch+" "*x+ch])
  return lst

