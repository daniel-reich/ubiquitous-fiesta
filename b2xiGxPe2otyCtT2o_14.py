
def how_many_times(msg):
  x = 0
  
  buchstaben = "abcdefghijklmnopqrstuvwxyz"
  buchstaben = list(buchstaben)
  
  msg = list(msg)
  for i in msg:
    pos = buchstaben.index(i) + 1
    x = x + pos
  return x

