
def counter():
  if hasattr(counter, 'c') == False:
    counter.c = -1
  counter.c += 1
  return counter.c

