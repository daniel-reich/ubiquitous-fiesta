
def generate_word(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append(["b","a"])
    
  Required = Parameters[0]
  Sequence = Parameters[1]
  
  if (Required < 2):
    return "invalid"
  
  elif (len(Sequence) >= Required):
    Link = ", "
    Answer = Link.join(Sequence)
    return Answer
  
  else:
    Upcoming = Sequence[-2] + Sequence[-1]
    Sequence.append(Upcoming)
    return generate_word(Required, Sequence)

