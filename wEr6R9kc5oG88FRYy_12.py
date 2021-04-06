
def get_frame(w, h, ch):
  if w <= 2 or h <= 2:
    return 'invalid'
  output = []
  output.append([ch*w])
  for i in range(h-2):
    output.append([ch + (' '*(w-2)) +ch])
  output.append([ch*w])
  return output

