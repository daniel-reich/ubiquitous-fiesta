
def spiral_transposition(lst):
  o = []
  i=0
  while lst:
    if i%4 == 0:
      o += lst.pop(0)
    elif i%4 == 1:
      o += [row.pop() for row in lst]
    elif i%4 == 2:
      o += lst.pop()[::-1]
    elif i%4 == 3:
      o += [row.pop(0) for row in lst][::-1]
    i += 1
  return o

