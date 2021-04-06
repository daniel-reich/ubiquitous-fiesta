
import functools
def magnitude(lst):
  if not lst:
    return 0
  return functools.reduce((lambda x,y: x+y),map(lambda x:x**2,lst))**(1/2.0)

