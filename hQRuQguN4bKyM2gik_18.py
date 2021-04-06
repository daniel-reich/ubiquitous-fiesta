
def simple_check(a, b):
  if a > b:
    larger = a
    smaller = b
  else:
    larger = b
    smaller = a
  counter = 0
  while smaller > 0:
    if larger % smaller == 0:
      counter +=1
    larger -= 1
    smaller -= 1
  return counter

