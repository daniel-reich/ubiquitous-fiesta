
def can_capture(queens):
  a,b = queens
  return a[0]==b[0] or a[1]==b[1] or abs(ord(a[0])-ord(b[0]))==abs(ord(a[1])-ord(b[1]))

