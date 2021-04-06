
def get_frame(w, h, ch):
  if w < 3 or h < 3:
    return "invalid"
  matrix = []
  matrix.append([w * ch])
  for i in range(h-2):
    matrix.append([ch + ((w-2) * " ") + ch])
  matrix.append([w * ch])
  return matrix

