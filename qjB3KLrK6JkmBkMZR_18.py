
def can_capture(queens):
  w,b = queens
  return w[0] == b[0] or w[1] == b[1] or  (ord(w[0])+int(w[1])) == (ord(b[0])+int(b[1])) or (ord(w[0])-int(w[1])) == (ord(b[0])-int(b[1]))

