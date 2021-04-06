
def fifth(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) < 5):
    return "Not enough arguments"
  else:
    return type(Parameters[4])

