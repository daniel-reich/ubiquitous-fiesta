
def get_frame(w, h, ch):
  frame = []
  if w <= 2 or h <= 2: return "invalid"
  for i in range(h):
    if i in [0, h - 1]: frame.append(["".join([ch] * w)])
    else: frame.append(["".join([ch] + ([" "] * (w -2)) + [ch])])
  return frame

