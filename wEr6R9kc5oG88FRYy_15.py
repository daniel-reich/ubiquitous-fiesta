
def get_frame(w, h, ch):
  if w < 3 or h < 3:
    return 'invalid'
  frame = [[w * ch]]
  mid = [ch + (' '*(w-2)) + ch]
  for i in range(h-2):
    frame.append(mid)
  frame.append([w * ch])
  return frame

