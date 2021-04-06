
def get_frame(w, h, ch):
  if w <= 2 or h <= 2:
    return "invalid"
  else:
    frame = []
    frame1 = []
    frame1.append(ch * w)
    frame.append(frame1)
    for i in range(0,(h-2)):
      frameN = []
      frameN.append(ch + (' ' * (w - 2)) + ch)
      frame.append(frameN)
    frame3 = []
    frame3.append(ch * w)
    frame.append(frame3)
    return frame

