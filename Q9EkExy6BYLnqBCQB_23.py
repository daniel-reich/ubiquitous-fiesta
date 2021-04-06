
def wrap_around(string, offset):
  if offset > 0:
    for i in range(offset):
      string = string[1:] + string[0]   
  else :
    for i in range(abs(offset)):
      string = string[-1] + string[0:-1]
  return string

