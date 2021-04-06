
def get_frame(w, h, ch):
  if w <= 2 or h <= 2: return "invalid"
  return [[ch*w]] + [["{0}{1}{0}".format(ch, ' '*(w-2))] for i in range(h-2)] + [[ch*w]]

