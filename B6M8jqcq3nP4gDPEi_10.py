
def iso_group(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Answer = []
    Answer.append(-999999)
    Parameters.append(Answer)
  
  Sample = Parameters[0]
  Answer = Parameters[1]
  
  if (Sample == []) and (len(Answer) == 1):
    return Answer[0]
  
  elif (Sample == []) and (len(Answer) > 1):
    return Answer
  
  elif (Sample[0] > Answer[0]):
    Answer = []
    Answer.append(Sample[0])
    return iso_group(Sample[1:], Answer)
  
  elif (Sample[0] == Answer[0]):
    Answer.append(Sample[0])
    return iso_group(Sample[1:], Answer)
  
  else:
    return iso_group(Sample[1:], Answer)

