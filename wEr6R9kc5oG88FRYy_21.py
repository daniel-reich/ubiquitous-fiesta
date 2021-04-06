
def get_frame(w, h, ch):
  matrix = []
  if w > 2 and h > 2:
    for i in range(h):
      if i == 0 or i == h-1:
        row = []
        row.append(ch*w)
        matrix.append(row)
      else:
        row = []
        row.append(ch + " "*(w-2) + ch)
        matrix.append(row)
  else:
    return "invalid"
  return matrix

