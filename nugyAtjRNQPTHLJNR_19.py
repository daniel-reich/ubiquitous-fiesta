
def pages_in_book(t):
  c,i = 0,0
  while c < t:
    c = i*(i-1)/2
    i += 1
  return c == t

