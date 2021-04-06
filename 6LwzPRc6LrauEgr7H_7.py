
def worm_length(worm):
  length = 0 
  
  
  for l in worm:
    if l != "-":
      return "invalid"
    else:
      length = length + 1
      
  
  if length == 0:
    return "invalid"
  else:
    length = length * 10
    string = str(length) + " " + "mm."
    return string

