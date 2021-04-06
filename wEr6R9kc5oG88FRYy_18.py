
def get_frame(w, h, ch):
  if w < 3 or h < 3:
    return "invalid"
  lst = []
  for i in range(0, h):
    lst.append([w*ch])
  for i in range(1,h-1):
    lst[i] = [ch + (w-2)*" " + ch]
  return lst

